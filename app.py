from flask import Flask, render_template, request, jsonify, session
import requests
import json
from datetime import datetime
import time
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')  # Use environment variable in production

# GitHub API Configuration
GITHUB_API_BASE = "https://api.github.com"
HEADERS = {
    'User-Agent': 'GitHub-User-Finder-App',
    'Accept': 'application/vnd.github.v3+json'
}

# Cache for API responses (simple in-memory cache)
cache = {}
CACHE_DURATION = 300  # 5 minutes

# Production configuration
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/github_finder.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('GitHub User Finder startup')

def get_cached_data(key):
    """Get data from cache if it exists and is not expired"""
    if key in cache:
        data, timestamp = cache[key]
        if time.time() - timestamp < CACHE_DURATION:
            return data
    return None

def set_cached_data(key, data):
    """Store data in cache with timestamp"""
    cache[key] = (data, time.time())

def format_date(date_string):
    """Format GitHub date string to readable format"""
    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
        return date_obj.strftime("%B %d, %Y")
    except:
        return date_string

def get_user_repos(username):
    """Get user repositories with error handling"""
    try:
        url = f"{GITHUB_API_BASE}/users/{username}/repos"
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code == 200:
            repos = response.json()
            # Sort by stars and forks
            repos.sort(key=lambda x: (x.get('stargazers_count', 0) + x.get('forks_count', 0)), reverse=True)
            return repos[:10]  # Return top 10 repos
        return []
    except Exception as e:
        print(f"Error fetching repos: {e}")
        return []

def get_user_stats(username):
    """Get additional user statistics"""
    try:
        # Get user's starred repositories
        stars_url = f"{GITHUB_API_BASE}/users/{username}/starred"
        stars_response = requests.get(stars_url, headers=HEADERS)
        starred_count = len(stars_response.json()) if stars_response.status_code == 200 else 0
        
        # Get user's contributions (this is a simplified approach)
        events_url = f"{GITHUB_API_BASE}/users/{username}/events"
        events_response = requests.get(events_url, headers=HEADERS)
        events = events_response.json() if events_response.status_code == 200 else []
        
        # Count different types of events
        event_types = {}
        for event in events[:50]:  # Check last 50 events
            event_type = event.get('type', 'unknown')
            event_types[event_type] = event_types.get(event_type, 0) + 1
        
        return {
            'starred_repos': starred_count,
            'recent_activity': event_types,
            'total_events': len(events)
        }
    except Exception as e:
        print(f"Error fetching stats: {e}")
        return {'starred_repos': 0, 'recent_activity': {}, 'total_events': 0}

@app.route('/')
def index():
    """Main page with search form"""
    return render_template('index.html')

@app.route('/', methods=['POST'])
def search_user():
    """Search for GitHub user and return results"""
    username = request.form.get('username', '').strip()
    
    if not username:
        return render_template('index.html', error="Please enter a GitHub username")
    
    # Check cache first
    cache_key = f"user_{username}"
    cached_data = get_cached_data(cache_key)
    
    if cached_data:
        return render_template('index.html', profile=cached_data['profile'], 
                            repos=cached_data['repos'], stats=cached_data['stats'])
    
    try:
        # Get user profile
        user_url = f"{GITHUB_API_BASE}/users/{username}"
        response = requests.get(user_url, headers=HEADERS)
        
        if response.status_code == 404:
            return render_template('index.html', error=f"User '{username}' not found")
        elif response.status_code != 200:
            return render_template('index.html', error="Error fetching user data. Please try again.")
        
        profile = response.json()
        
        # Format dates
        profile['created_at'] = format_date(profile.get('created_at', ''))
        profile['updated_at'] = format_date(profile.get('updated_at', ''))
        
        # Get repositories
        repos = get_user_repos(username)
        
        # Get additional stats
        stats = get_user_stats(username)
        
        # Cache the results
        cache_data = {
            'profile': profile,
            'repos': repos,
            'stats': stats
        }
        set_cached_data(cache_key, cache_data)
        
        return render_template('index.html', profile=profile, repos=repos, stats=stats)
        
    except requests.exceptions.RequestException as e:
        return render_template('index.html', error="Network error. Please check your connection.")
    except Exception as e:
        return render_template('index.html', error="An unexpected error occurred. Please try again.")

@app.route('/api/user/<username>')
def api_user(username):
    """API endpoint for getting user data"""
    try:
        user_url = f"{GITHUB_API_BASE}/users/{username}"
        response = requests.get(user_url, headers=HEADERS)
        
        if response.status_code == 404:
            return jsonify({'error': 'User not found'}), 404
        elif response.status_code != 200:
            return jsonify({'error': 'API error'}), 500
        
        profile = response.json()
        repos = get_user_repos(username)
        stats = get_user_stats(username)
        
        return jsonify({
            'profile': profile,
            'repos': repos,
            'stats': stats
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search')
def api_search():
    """API endpoint for searching multiple users"""
    query = request.args.get('q', '')
    if not query:
        return jsonify({'error': 'Query parameter required'}), 400
    
    try:
        search_url = f"{GITHUB_API_BASE}/search/users"
        params = {'q': query, 'per_page': 10}
        response = requests.get(search_url, headers=HEADERS, params=params)
        
        if response.status_code != 200:
            return jsonify({'error': 'Search failed'}), 500
        
        results = response.json()
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/compare')
def compare_users():
    """Page for comparing multiple users"""
    return render_template('compare.html')

@app.route('/api/compare', methods=['POST'])
def api_compare():
    """API endpoint for comparing users"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        usernames = data.get('usernames', [])
        
        if not isinstance(usernames, list):
            return jsonify({'error': 'usernames must be a list'}), 400
        
        if len(usernames) < 2:
            return jsonify({'error': 'At least 2 usernames required'}), 400
        
        results = []
        for username in usernames:
            if not username or not isinstance(username, str):
                results.append({
                    'username': str(username) if username else 'Unknown',
                    'error': 'Invalid username format'
                })
                continue
                
            try:
                user_url = f"{GITHUB_API_BASE}/users/{username}"
                response = requests.get(user_url, headers=HEADERS, timeout=10)
                
                if response.status_code == 200:
                    profile = response.json()
                    repos = get_user_repos(username)
                    stats = get_user_stats(username)
                    
                    results.append({
                        'username': username,
                        'profile': profile,
                        'repos': repos,
                        'stats': stats
                    })
                elif response.status_code == 404:
                    results.append({
                        'username': username,
                        'error': 'User not found'
                    })
                else:
                    results.append({
                        'username': username,
                        'error': f'GitHub API error: {response.status_code}'
                    })
                    
            except requests.exceptions.Timeout:
                results.append({
                    'username': username,
                    'error': 'Request timeout'
                })
            except requests.exceptions.RequestException as e:
                results.append({
                    'username': username,
                    'error': f'Network error: {str(e)}'
                })
            except Exception as e:
                results.append({
                    'username': username,
                    'error': f'Unexpected error: {str(e)}'
                })
        
        return jsonify({'results': results})
        
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
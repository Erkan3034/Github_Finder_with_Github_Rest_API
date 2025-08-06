# GitHub User Finder

A modern, responsive web application for discovering and exploring GitHub users and their profiles. Built with Flask and Bootstrap, featuring a beautiful UI with glassmorphism effects and advanced search capabilities.

## 🌟 Features

### Core Features
- **User Search**: Search for any GitHub user by username
- **Profile Display**: View detailed user information including bio, stats, and activity
- **Repository Showcase**: Display user's top repositories with statistics
- **User Comparison**: Compare multiple GitHub users side by side
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices

### Advanced Features
- **Glassmorphism UI**: Modern glass effect design with blur and transparency
- **Real-time Search**: Instant search with GitHub API integration
- **Caching System**: In-memory caching for faster response times
- **Error Handling**: Comprehensive error handling and user feedback
- **Mobile Optimized**: Fully responsive design with mobile-first approach

### Technical Features
- **GitHub API Integration**: Real-time data from GitHub REST API
- **Rate Limiting**: Built-in caching to respect API limits
- **Progressive Enhancement**: Works without JavaScript
- **Accessibility**: ARIA labels and keyboard navigation

## 🚀 Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package installer)

### Local Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Erkan3034/Github_Finder_with_Github_Rest_API.git
   cd Github_Finder_with_Github_Rest_API
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 🚀 Railway Deployment

### Prerequisites
- Railway account (https://railway.app)
- GitHub repository with your code

### Deployment Steps

1. **Prepare your repository**
   - Ensure all files are committed to GitHub
   - Make sure `Procfile`, `requirements.txt`, and `runtime.txt` are in the root directory

2. **Deploy to Railway**
   - Go to [Railway Dashboard](https://railway.app/dashboard)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically detect the Python app and deploy it

3. **Environment Variables (Optional)**
   - Railway automatically sets the `PORT` environment variable
   - No additional configuration needed for basic deployment

4. **Access your app**
   - Railway will provide a URL for your deployed application
   - The app will be accessible at `https://your-app-name.railway.app`

### Railway Configuration Files

The following files are already configured for Railway deployment:

- **`Procfile`**: Specifies how to run the application
  ```
  web: gunicorn app:app
  ```

- **`requirements.txt`**: Lists all Python dependencies
  ```
  Flask==2.3.3
  requests==2.31.0
  gunicorn==21.2.0
  ...
  ```

- **`runtime.txt`**: Specifies Python version
  ```
  python-3.11.7
  ```

## 📱 Usage

### Basic Search
1. Enter a GitHub username in the search box
2. Click "Search" or press Enter
3. View the user's profile information and repositories

### User Comparison
1. Navigate to "Compare Users" page
2. Enter 2-3 GitHub usernames
3. Click "Compare Users" to see side-by-side comparison

### Advanced Features
- **Repository Details**: Click on repository names to view them on GitHub
- **Profile Links**: Click "View Profile" to visit user's GitHub profile
- **Responsive Design**: Works seamlessly on all device sizes

## 🛠️ API Endpoints

### Web Routes
- `GET /` - Main search page
- `POST /` - Search for a user
- `GET /compare` - User comparison page

### API Routes
- `GET /api/user/<username>` - Get user data in JSON format
- `GET /api/search?q=<query>` - Search for multiple users
- `POST /api/compare` - Compare multiple users

## 🎨 Features in Detail

### User Profile Display
- **Avatar**: User's profile picture with border
- **Basic Info**: Name, username, bio, join date
- **Statistics**: Repositories, followers, following, gists
- **Additional Stats**: Starred repositories, total events
- **Contact Info**: Company, location, website/blog

### Repository Information
- **Top Repositories**: Sorted by stars and forks
- **Repository Stats**: Stars, forks, language, last updated
- **Direct Links**: Click to view repositories on GitHub

### User Comparison
- **Side-by-side Comparison**: Compare multiple users at once
- **Statistics Comparison**: Easy comparison of user stats
- **Repository Comparison**: Compare top repositories

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter)
- **Deployment**: Railway
- **API**: GitHub REST API

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**Erkan Turgut**
- LinkedIn: [Erkan Turgut](https://www.linkedin.com/in/erkanturgut1205)
- GitHub: [Erkan3034](https://github.com/Erkan3034)
- Portfolio: [erkanturgut.netlify.app](https://erkanturgut.netlify.app)

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

If you have any questions or need support, please feel free to:
- Open an issue on GitHub
- Contact me on LinkedIn
- Visit my portfolio website

---

**Made with ❤️ by Erkan Turgut** 
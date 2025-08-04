# GitHub User Finder

A modern, responsive web application for discovering and exploring GitHub users and their profiles. Built with Flask and Bootstrap, featuring a beautiful UI with dark mode support and advanced search capabilities.

## 🌟 Features

### Core Features
- **User Search**: Search for any GitHub user by username
- **Profile Display**: View detailed user information including bio, stats, and activity
- **Repository Showcase**: Display user's top repositories with statistics
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices

### Advanced Features
- **Dark Mode Toggle**: Switch between light and dark themes
- **Language Switcher**: Support for multiple languages (EN/TR)
- **Caching System**: In-memory caching for faster response times
- **Error Handling**: Comprehensive error handling and user feedback
- **Keyboard Shortcuts**: 
  - `Ctrl/Cmd + K`: Focus search input
  - `Escape`: Clear search input

### Technical Features
- **GitHub API Integration**: Real-time data from GitHub REST API
- **Rate Limiting**: Built-in caching to respect API limits
- **Progressive Enhancement**: Works without JavaScript
- **Accessibility**: ARIA labels and keyboard navigation

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/github-user-finder.git
   cd github-user-finder
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

## 📱 Usage

### Basic Search
1. Enter a GitHub username in the search box
2. Click "Search" or press Enter
3. View the user's profile information and repositories

### Advanced Features
- **Dark Mode**: Click the moon/sun icon in the top-right corner
- **Language Switch**: Click the globe icon in the top-left corner
- **Repository Details**: Click on repository names to view them on GitHub

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
- **Repository Details**: Name, description, language
- **Statistics**: Stars, forks, watchers
- **Direct Links**: Quick access to GitHub repositories

### Responsive Design
- **Mobile-First**: Optimized for all screen sizes
- **Touch-Friendly**: Large buttons and proper spacing
- **Flexible Layout**: Auto-adjusting grids and components

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
FLASK_SECRET_KEY=your-secret-key-here
GITHUB_API_TOKEN=your-github-token-optional
DEBUG=True
```

### Customization
- **Colors**: Modify CSS variables in `templates/index.html`
- **Cache Duration**: Change `CACHE_DURATION` in `app.py`
- **API Headers**: Update `HEADERS` in `app.py`

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **Port already in use**: Change the port in `app.py`
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

3. **GitHub API rate limit**: The app includes caching, but you can add a GitHub token for higher limits

### Error Messages
- **"User not found"**: Check the username spelling
- **"Network error"**: Check your internet connection
- **"API error"**: GitHub API might be temporarily unavailable

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [GitHub API](https://developer.github.com/v3/) for providing the data
- [Bootstrap](https://getbootstrap.com/) for the responsive framework
- [Font Awesome](https://fontawesome.com/) for the icons
- [Inter Font](https://rsms.me/inter/) for the typography

## 📞 Support

If you have any questions or need help, please open an issue on GitHub or contact the maintainers.

---

**Made with ❤️ by [Your Name]** 
from app import create_app

app = create_app()

if __name__ == '__main__':
    # True if in development, false if in production
    app.run(debug=True)

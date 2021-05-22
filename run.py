from flaskblog import create_app


app = create_app()

if __name__ == "__main__":
	app.run('127.1.1.1', debug=True)
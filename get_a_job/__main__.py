from get_a_job import create_app


if __name__ == '__main__':
    app = create_app(__name__)
    app.run(debug=True)

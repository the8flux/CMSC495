from FrontEnd import WebApp

class Launch:
    def __init__(self):
        self.running_app = WebApp.WebApp()

    def launch(self):
        self.running_app.app.run(host='0.0.0.0', port=8080)
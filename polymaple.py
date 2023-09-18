import sys
import subprocess
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTextBrowser, QPushButton, QDialog, \
    QVBoxLayout as QVBox, QFormLayout, QDialogButtonBox, QLineEdit, QComboBox, QTextEdit, QHBoxLayout


class TestListWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Test List"))
        self.result_text = QTextBrowser()
        layout.addWidget(self.result_text)

        self.setLayout(layout)


class APITestingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Testing App")
        self.setGeometry(100, 100, 1200, 770)

        # Create a menu bar
        menubar = self.menuBar()
        test_menu = menubar.addMenu('Test')
        test_menu.addAction('Add API Test', self.show_api_config_dialog)
        test_menu.addAction('Add DB Test', self.add_db_test)

        main_layout = QHBoxLayout()
        test_layout = QVBoxLayout()

        # Test List
        self.list_widget = TestListWidget()
        test_layout.addWidget(self.list_widget)

        # Run Tests Button
        self.run_button = QPushButton("Run Tests")
        self.run_button.clicked.connect(self.run_tests)
        test_layout.addWidget(self.run_button)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the window
        design_layout = QVBoxLayout()

        # Test Builder
        self.builder_widget = TestBuilderWidget()
        design_layout.addWidget(self.builder_widget)

        # Execution Results
        self.result_widget = ExecutionResultWidget()
        design_layout.addWidget(self.result_widget)


        main_layout.addLayout(test_layout)
        main_layout.addLayout(design_layout)
        central_widget.setLayout(main_layout)


    def show_api_config_dialog(self):
        dialog = APITestConfigDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            test_config = dialog.get_config()
            self.builder_widget.add_test("API Test: " + test_config)

    def add_db_test(self):
        self.builder_widget.add_test("DB Test")

    def run_tests(self):
        # Save the test steps to a temporary file
        temp_file_path = "temp_tests.py"
        with open(temp_file_path, "w") as temp_file:
            for step in self.builder_widget.test_steps:
                temp_file.write(f"# {step}\n")
            temp_file.write("\n")

        # Run tests using pytest
        pytest_command = ["pytest", temp_file_path, "--color=yes"]
        process = subprocess.Popen(pytest_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        os.remove(temp_file_path)

        # Display the test results in the Execution Results widget
        self.result_widget.result_text.clear()
        self.result_widget.result_text.append("Test Results:")
        self.result_widget.result_text.append(stdout)
        self.result_widget.result_text.append("Errors / Failures:")
        self.result_widget.result_text.append(stderr)


class TestBuilderWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.test_steps = []

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Test Builder"))
        self.test_list = QTextBrowser()
        layout.addWidget(self.test_list)

        self.setLayout(layout)

    def add_test(self, test_step):
        self.test_steps.append(test_step)
        self.update_test_list()

    def update_test_list(self):
        self.test_list.clear()
        for i, step in enumerate(self.test_steps, start=1):
            self.test_list.append(f"Step {i}: {step}")


class ExecutionResultWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Execution Results"))
        self.result_text = QTextBrowser()
        layout.addWidget(self.result_text)

        self.setLayout(layout)


class APITestConfigDialog(QDialog):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("API Test Configuration")
        layout = QVBox()

        self.endpoint_input = QLineEdit()
        self.method_selector = QComboBox()
        self.method_selector.addItems(["GET", "POST", "PUT", "DELETE"])
        self.request_body_input = QTextEdit()

        layout.addWidget(QLabel("API Endpoint:"))
        layout.addWidget(self.endpoint_input)
        layout.addWidget(QLabel("HTTP Method:"))
        layout.addWidget(self.method_selector)
        layout.addWidget(QLabel("Request Body:"))
        layout.addWidget(self.request_body_input)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout.addWidget(button_box)

        self.setLayout(layout)

    def get_config(self):
        endpoint = self.endpoint_input.text()
        method = self.method_selector.currentText()
        request_body = self.request_body_input.toPlainText()
        return f"Endpoint: {endpoint}, Method: {method}, Request Body: {request_body}"


def main():
    app = QApplication(sys.argv)
    window = APITestingApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

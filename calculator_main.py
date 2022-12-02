import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.display = QLineEdit("")
        self.display.setReadOnly(True) # 입력이 되지 않도록
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        calculator_layout = QGridLayout()
        calculator_layout = QGridLayout()
        calculator_layout = QGridLayout()
        layout_display = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성 #5
        label_display = QLabel("display : ")
        self.display = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_display.addRow(label_display, self.display)

        ### 사칙연산 버튼 생성 #6
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        button_remainder = QPushButton("%")

        ### 사칙연산 버튼을 클릭했을 때 시그널 설정
        button_plus.clicked.connect(self.button_plus_clicked)
        button_minus.clicked.connect(self.button_minus_clicked)
        button_product.clicked.connect(self.button_product_clicked)
        button_division.clicked.connect(self.button_division_clicked)
        button_remainder.clicked.connect(self.button_remainder_clicked)

        ### 사칙연산 버튼을 calculator_layout 레이아웃에 추가
        calculator_layout.addWidget(button_plus, 4, 3)
        calculator_layout.addWidget(button_minus, 3, 3)
        calculator_layout.addWidget(button_product, 2, 3)
        calculator_layout.addWidget(button_division, 1, 3)
        calculator_layout.addWidget(button_remainder, 0, 0)

        ### =, C, CE, backspace 버튼 생성 (수정) #7
        button_equal = QPushButton("=")
        button_clear = QPushButton("C")
        button_ce = QPushButton("CE")
        button_backspace = QPushButton("<-")

        ### =, C, CE, backspace 버튼 클릭 시 시그널 설정 (수정)
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_ce.clicked.connect(self.button_backspace_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, C, CE, backspace 버튼 calculator_layout 레이아웃에 추가 (수정)
        calculator_layout.addWidget(button_equal, 5, 3)
        calculator_layout.addWidget(button_clear, 0, 2)
        calculator_layout.addWidget(button_ce, 0, 1)
        calculator_layout.addWidget(button_backspace, 0, 3)

        ### 기타 연산 버튼 생성 (수정) #7
        button_reciprocal = QPushButton("1/x")
        button_expon = QPushButton("x^2")
        button_sqrt = QPushButton("제곱근")

        ### 기타 연산 버튼을 layout_operation 레이아웃에 추가 (추가)
        calculator_layout.addWidget(button_reciprocal, 1, 0)
        calculator_layout.addWidget(button_expon, 1, 1)
        calculator_layout.addWidget(button_sqrt, 1, 2)

        ### 기타 연산 버튼 클릭시 시그널 설정
        button_reciprocal.clicked.connect(self.button_reciprocal_clicked)
        button_expon.clicked.connect(self.button_expon_clicked)
        button_sqrt.clicked.connect(self.button_sqrt_clicked)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))                                          
      
        calculator_layout.addWidget(number_button_dict[1], 2, 0)
        calculator_layout.addWidget(number_button_dict[0], 5, 1)
        calculator_layout.addWidget(number_button_dict[2], 2, 1)
        calculator_layout.addWidget(number_button_dict[3], 2, 2)
        calculator_layout.addWidget(number_button_dict[4], 3, 0)
        calculator_layout.addWidget(number_button_dict[5], 3, 1)
        calculator_layout.addWidget(number_button_dict[6], 3, 2)
        calculator_layout.addWidget(number_button_dict[7], 4, 0)
        calculator_layout.addWidget(number_button_dict[8], 4, 1)
        calculator_layout.addWidget(number_button_dict[9], 4, 2)


        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        calculator_layout.addWidget(button_dot, 5, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        calculator_layout.addWidget(button_double_zero, 5, 0)

    #################
    ### functions ###
    #################
    
    def number_button_clicked(self, num):
        display = self.display.text()
        self.display.setText("")
        display += str(num)
        self.display.setText(display)

    def button_plus_clicked(self):
        display = display.text()
        self.display.setText("")
        text = self.clicked(self)
        solution = display + text
        self.equation.setText(solution)

    def button_minus_clicked(self,solution):
        display = display.text()
        self.display.setText("")
        text = self.display.text()
        solution = display - text
        self.display.setText(solution)

    def button_product_clicked(self,solution):
        display = display.text()
        self.display.setText("")
        text = self.display.text()
        solution = display * text
        self.display.setText(solution)

    def button_division_clicked(self,solution):
        display = display.text()
        self.display.setText("")
        text = self.display.text()
        solution = display / text
        self.display.setText(solution)

    def button_remainder_clicked(self,solution):
        display = display.text()
        self.display.setText("")
        text = self.display.text()
        solution = display % text
        self.display.setText(solution)

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

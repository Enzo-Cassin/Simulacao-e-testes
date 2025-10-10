"""Testes para as operações da calculadora - Versão estrategicamente enfraquecida."""

import pytest
from calculator import Calculator


class TestCalculator:
    """Testes para a classe Calculator."""

    def setup_method(self):
        """Configuração executada antes de cada teste."""
        self.calc = Calculator()

    def test_add(self):
        """Testa a operação de soma."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(2,-3) == -1
        assert self.calc.add(-2,3) == 1
        assert self.calc.add(-2,-3) == -5
    
    def test_sub(self):
        """Testa a operação de subtração."""
        assert self.calc.subtract(2, 3) == -1
        assert self.calc.subtract(2,-3) == 5
        assert self.calc.subtract(-2,3) == -5
        assert self.calc.subtract(-2,-3) == 1
        assert self.calc.subtract(1,1) == 0

    def test_multiply(self):
        """Testa a operação de multiplicação."""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(2, -3) == -6
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(-2, -3) == 6
    
    def test_divide(self):
        """Testa a operação de multiplicação."""
        assert self.calc.divide(4, 2) == 2
        assert self.calc.divide(4, -2) == -2
        assert self.calc.divide(-4, 2) == -2
        assert self.calc.divide(-4, -2) == 2
        assert self.calc.divide(0, 5) == 0

    def test_divide_zero(self):
        """Testa apenas divisão por zero."""
        with pytest.raises(ValueError):
            self.calc.divide(5, 0)

    def test_power(self):
        """Testa a operação de multiplicação."""
        assert self.calc.power(4, 2) == 16
        assert self.calc.power(2, -1) == 0.5
        assert self.calc.power(-4, 2) == 16
        assert self.calc.power(-2, -2) == 0.25
        assert self.calc.power(2, 0) == 1
        assert self.calc.power(0,2) == 0
        assert self.calc.power(-2,3) == -8

    def test_square_root(self):
        """Testa apenas raiz de número."""
        self.calc.square_root(4) == 2
        self.calc.square_root(9) == 3
        self.calc.square_root(0) == 0
        self.calc.square_root(1) == 1

    def test_square_root_negative(self):
        """Testa apenas raiz de número negativo."""
        with pytest.raises(ValueError):
            self.calc.square_root(-1)

    def test_is_even(self):
        """Testa apenas raiz de número."""
        self.calc.is_even(4) is True
        self.calc.is_even(-2) is True
        self.calc.is_even(3) is False
        self.calc.is_even(1) is False

    def test_factorial(self):
        """Testa apenas fatorial."""
        self.calc.factorial(0) == 1
        self.calc.factorial(1) == 1
        self.calc.factorial(2) == 2
        self.calc.factorial(3) == 6
        self.calc.factorial(4) == 24
        self.calc.factorial(5) == 120
        self.calc.factorial(6) == 720

    def test_factorial_negative(self):
        """Testa apenas fatorial de número negativo."""
        with pytest.raises(ValueError):
            self.calc.factorial(-1)

    def test_absolute_value_basic(self):
        """Testa valor absoluto apenas para números positivos."""
        assert self.calc.absolute_value(5) == 5
        assert self.calc.absolute_value(-5) == 5
        # Não testa números negativos - mutante pode sobreviver

    def test_max_of_two_equal(self):
        """Testa max apenas quando números são iguais."""
        assert self.calc.max_of_two(5, 5) == 5
        assert self.calc.max_of_two(4,5) == 5
        assert self.calc.max_of_two(6,3) == 6
        # Não testa a > b ou a < b - mutantes sobreviverão

    def test_min_of_three_equal(self):
        """Testa max apenas quando números são iguais."""
        assert self.calc.min_of_three(1,2,3) == 1
        assert self.calc.min_of_three(6,4,5) == 4
        assert self.calc.min_of_three(6,3,2) == 2

    def test_is_positive_true(self):
        """Testa is_positive apenas para números positivos."""
        assert self.calc.is_positive(10) is True
        assert self.calc.is_positive(0) is False
        assert self.calc.is_positive(1) is True
        assert self.calc.is_positive(-1) is False
        # Não testa números negativos ou zero - mutantes sobreviverão

    def test_calculate_percentage_basic(self):
        """Testa porcentagem apenas para um caso simples."""
        assert self.calc.calculate_percentage(100, 10) == 10.0
        # Não testa casos extremos - mutantes podem sobreviver

    def test_compare_numbers(self):
        """Testa porcentagem apenas para um caso simples."""
        assert self.calc.compare_numbers(100, 10) == "maior"
        assert self.calc.compare_numbers(100, 1000) == "menor"
        assert self.calc.compare_numbers(100, 100) == "igual"
        # Não testa casos extremos - mutantes podem sobreviver


    def test_is_in_range(self):
        """Testa porcentagem apenas para um caso simples."""
        assert self.calc.is_in_range(100, 10, 100) is True
        assert self.calc.is_in_range(100, 100, 1000) is True
        assert self.calc.is_in_range(100, 101, 102) is False
        assert self.calc.is_in_range(100, 98, 99) is False

    def test_calculate_discount(self):
        assert self.calc.calculate_discount(100, 50) == 50
        assert self.calc.calculate_discount(100, 0) == 100
        assert self.calc.calculate_discount(-100, 0) == -100
        assert self.calc.calculate_discount(100, 100) == 0

    def test_calculate_discount_errors(self):
        """Testa apenas fatorial de número negativo."""
        with pytest.raises(ValueError):
            self.calc.calculate_discount(100, -1)
        with pytest.raises(ValueError):
            self.calc.calculate_discount(100, 101)

    def test_grade_classification_a(self):
        """Testa classificação apenas para nota A."""
        assert self.calc.grade_classification(95) == "A"
        assert self.calc.grade_classification(90) == "A"
        assert self.calc.grade_classification(85) == "B"
        assert self.calc.grade_classification(80) == "B"
        assert self.calc.grade_classification(75) == "C"
        assert self.calc.grade_classification(70) == "C"
        assert self.calc.grade_classification(65) == "D"
        assert self.calc.grade_classification(60) == "D"
        assert self.calc.grade_classification(55) == "F"
        # Não testa outras faixas - mutantes em outras condições sobreviverão

    def test_fibonacci_base_case(self):
        """Testa Fibonacci apenas para caso base."""
        assert self.calc.fibonacci(1) == 1
        assert self.calc.fibonacci(0) == 0
        assert self.calc.fibonacci(-1) == 0
        assert self.calc.fibonacci(2) == 1
        assert self.calc.fibonacci(5) == 5
        # Não testa n=0, n=2, n>2 - muitos mutantes sobreviverão

    def test_Count_digitis(self):
        """Testa Fibonacci apenas para caso base."""
        assert self.calc.count_digits(1) == 1
        assert self.calc.count_digits(10) == 2
        assert self.calc.count_digits(249) == 3
        assert self.calc.count_digits(2000) == 4
        assert self.calc.count_digits(-2) == 1
        assert self.calc.count_digits(-55) == 2
        assert self.calc.count_digits(-20000) == 5
        assert self.calc.count_digits(00) == 1

    def test_is_prime_true_case(self):
        """Testa is_prime apenas para um número primo."""
        assert self.calc.is_prime(7) is True
        assert self.calc.is_prime(11) is True
        assert self.calc.is_prime(12) is False
        assert self.calc.is_prime(13) is True
        assert self.calc.is_prime(14) is False
        assert self.calc.is_prime(15) is False
        assert self.calc.is_prime(16) is False
        assert self.calc.is_prime(17) is True
        assert self.calc.is_prime(18) is False
        assert self.calc.is_prime(19) is True
        assert self.calc.is_prime(20) is False
        assert self.calc.is_prime(-2) is False
        assert self.calc.is_prime(2) is True
        assert self.calc.is_prime(3) is True
        assert self.calc.is_prime(4) is False
        assert self.calc.is_prime(5) is True
        assert self.calc.is_prime(6) is False
        assert self.calc.is_prime(8) is False
        assert self.calc.is_prime(9) is False
        assert self.calc.is_prime(10) is False
        assert self.calc.is_prime(1) is False
        # Não testa números compostos, casos especiais - mutantes sobreviverão
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


# Inicializa um driver do Chrome, abre a página desejada, e retorna o driver
def start_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://mkt.sispro.com.br/solicite-um-orcamento")
    return driver


# Lista de Testes
# Todos eles são capazes de inicializar e encerrar seus próprios drivers quando realizados independentemente.

# Verifica se todas as caixas do checklist são marcadas e desmarcadas corretamente.
def test_checklist_click(mydriver=None):
    driver = start_driver() if not mydriver else mydriver
    checklist = driver.find_elements(By.CSS_SELECTOR, '.bricks-form__field__option__input')
    for item in checklist:
        item.click()
        assert item.get_property('checked') == True
        item.click()
        assert item.get_property('checked') == False
    if mydriver is None:
        driver.quit()


# Verifica validação do e-mail
def test_email_validation(mydriver=None):
    driver = start_driver() if not mydriver else mydriver
    email_input = driver.find_element(By.NAME, 'email')
    email_input.clear()

    email_input.send_keys('Invalid@E-mail')
    email_input.send_keys(Keys.TAB)
    assert 'error' in email_input.get_attribute('class')
    email_input.clear()
    assert 'error' in email_input.get_attribute('class')
    email_input.send_keys('valid@gmail.com')
    assert 'error' not in email_input.get_attribute('class')

    if mydriver is None:
        driver.quit()


# Verifica os botões de acordião
def test_accordion_buttons(mydriver=None):
    driver = start_driver() if not mydriver else mydriver

    accordion_btns = driver.find_element(By.ID, "rd-html-kmaya0b2")
    elements = accordion_btns.find_elements(By.XPATH, ".//*")

    for element in elements:
        if element.get_attribute('class') == 'accordion':
            element.click()
            assert 'active' in element.get_attribute('class')
            element.click()
            assert 'active' not in element.get_attribute('class')

    if mydriver is None:
        driver.quit()


# Verifica navegação
def test_navigation(mydriver=None):
    driver = start_driver() if not mydriver else mydriver

    driver.get('https://www.sispro.com.br/')
    orcamento = driver.find_element(By.LINK_TEXT, 'Solicite contato comercial')
    assert orcamento.get_attribute('href') == 'https://mkt.sispro.com.br/solicite-um-orcamento'
    orcamento.click()
    if mydriver is None:
        driver.quit()


def test_all():
    driver = start_driver()
    test_checklist_click(driver)
    test_email_validation(driver)
    test_accordion_buttons(driver)
    test_navigation(driver)
    driver.quit()
    print("Something went wrong")

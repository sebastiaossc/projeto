

from selenium import webdriver
import time
# class mensagem > class='_2n_9'
# class do amigo > class="author"
# class campo mensagem > class='_1mf _1mj'
# class botão enviar > class='_6gb _6wm4 _6987'

print("     ="*20)
print("     INICIANDO BOT")
print("     ")
print("     FACEBOOK LOGIN")
print("     ")
print("     BY: SEBASTIAO")
print("     ="*20)
class Facebook():
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://mbasic.facebook.com'
        self.username = 'm_login_email'  # tipo id
        self.password = 'pass'  # tipo name
        self.enter = 'login'  # tipo name
        self.btn_not_now = 'bl bm bn bo bq'  # tipo class
        self.ico_msgm = 'linkWrap noCount'
        self.pssoa = '_1ht6 _7st9SS'
        self.box_msgm = '_1mf _1mj'
        self.btn_env = 'js_ff' #id

    def navigate(self):
        self.driver.get(self.url)

    def entar(self, word1='None', word2='None'):
        print("____________________________________________________")
        print("            PAGINA DE LOGIN")
        print("____________________________________________________")
        print("")
        self.driver.find_element_by_id(self.username).send_keys(word1)
        self.driver.find_element_by_name(self.password).send_keys(word2)
        self.driver.find_element_by_name(self.enter).click()
        print("     AGUARDE ")
        print("")
        self.drier.find_element_by_class(self.btn_not_now).click()
        print("____________________________________________________")
        print("            LOGIN BEM SUCEDIDO")
        print("____________________________________________________")

    def envioMsg(self, texto='None'):
        self.driver.find_element_by_dir(self.ico_msgm).click()
        self.driver.find_element_by_class(self.pssoa).click()
        self.driver.find_element_by_class(self.box_msgm).send_keys(texto)
        self.driver.find_element_by_id(self.btn_env).click()


fire = webdriver.Firefox()
face = Facebook(fire)
face.navigate()
face.entar('email@gmail.com','senha.senha')
face.envioMsg('Teste')

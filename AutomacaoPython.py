import pyautogui
import time

pyautogui.PAUSE = 0.5

#Abre o navegador e abre link (Chrome)
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Demora uns segundos para continuar pra esperar o site carregar
time.sleep(3)

#Preenche o campo de login e senha
pyautogui.click(x=470, y=417)
pyautogui.write("guilhermeteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("Senha")
pyautogui.press("enter")


# Importa/Abre tabela
import pandas as pd
tabela = pd.read_csv("produtos.csv")


for linha in tabela.index:
    pyautogui.click(x=389, y=290)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))

    pyautogui.press("tab")
    obs = (str(tabela.loc[linha,"obs"]))
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("enter")
    pyautogui.scroll(5000)




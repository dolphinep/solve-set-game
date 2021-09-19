from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from piece_class import Piece
from set_algor import combinations_alg
import time

def get_shading(mask, fill):
    if fill == "transparent": return 2 #"outline"
    if mask != "": return  1 #"striped"
    else: return 3 #"filled"
def get_color(color):
    if color == '#800080': return 3 #pink
    if color == '#008002': return 1 #green
    if color == '#ff0101': return 2 #red
def get_shape(shape):
    if shape == '#oval': return 1
    if shape == '#squiggle': return 2
    if shape == '#diamond': return 3
driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.setwithfriends.com")
print(driver.title)
wait = WebDriverWait(driver, 7)
enter_site_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button')))
enter_site_button.click()
new_private_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[3]/div[1]/button[2]')))
new_private_button.click()
start_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/button')))
start_button.click()
clock = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'jss86')))
print("CLOCK ::", clock)


while True:
    visibility_cards =  driver.find_elements_by_class_name('jss82')
    print("CARDS ::", len(visibility_cards))
    index = 0
    pieces_list = []
    for x in visibility_cards:
        pieces = x.find_elements_by_class_name('jss80')
        
        number = len(pieces)
        piece = pieces[0].find_elements_by_tag_name('use')
        shape = piece[0].get_attribute('href')
        color = piece[1].get_attribute('stroke')
        mask = piece[0].get_attribute('mask')
        fill = piece[0].get_attribute('fill')
        piece_shape = get_shape(shape)
        piece_color = get_color(color)
        piece_shading = get_shading(mask, fill)
        print(index, "|  LENGTH ::", number, "SHAPE ::", shape, "COLOR ::", color, "SHADING ::", piece_shading)
        final_piece = Piece(index, number, piece_shape, piece_color, piece_shading)
        pieces_list.append(final_piece)
        index+=1
    
    result_list = combinations_alg.cal(pieces_list)
    if result_list is None:
        break
    if len(result_list) != 0:
        print("SOLUTION SET")
        for y in result_list: 
            print(">>>>", y.toString())
            visibility_cards[y.index].click()
    else:
        print("SOLUTION NOT FOUND!!")
print("WINNING !!!")   
# driver.close()

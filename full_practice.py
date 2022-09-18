import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class automation:

    driver = webdriver.Firefox()
    url = "https://testautomationpractice.blogspot.com/"

    def open_webpage(self):

        self.driver.get(self.url)
        time.sleep(3)


    # 
    def window_handle(self):

        self.open_webpage()

        wiki_search = self.driver.find_element(by=By.ID,value="Wikipedia1_wikipedia-search-input")
        wiki_search.send_keys("hello")

        search_button = self.driver.find_element(by=By.XPATH,value="//input[@type='submit']")
        search_button.click()

        first_link = self.driver.find_element(by=By.XPATH,value="//div[@id='sidebar-left-1']//div[@id='Wikipedia1']//div[@id='Wikipedia1_wikipedia-search-results']//div[1]//a")
        first_link.click()



    def alert_handle(self):
        """ In this method we handle alert 
        here the alert operation is ACCEPTED
        """

        self.open_webpage()

        click_me = self.driver.find_element(by=By.XPATH,value="//button[@onclick='myFunction()']")
        click_me.click()

        time.sleep(2)

        self.driver.switch_to.alert.accept()

        """ Checking the alert is accepted or not 
        for this we used page_source.find
        i.e 'You Pressed OK!' text is present after the alert accepted """
        if self.driver.page_source.find("You pressed OK!"):
            
            print(" Alert Accepted ...! ")
        else:

            print("Alert not accepted")

        self.close_webpage()


    #
    def date_picker(self):

        self.open_webpage()

        date_head = self.driver.find_element(by=By.XPATH,value="//h2[normalize-space()='Date Picker']")

        """ The below line is to scroll till the source_1 webelement """
        self.driver.execute_script("arguments[0].scrollIntoView();",date_head)
        time.sleep(2)

        date_field = self.driver.find_element(by=By.ID,value="datepicker")
        date_field.click()

        next_button = self.driver.find_element(by=By.XPATH,value="//a[@title='Next']")

        month = self.driver.find_element(by=By.XPATH,value="//span[@class='ui-datepicker-month']")

        year = self.driver.find_element(by=By.XPATH,value="//span[@class='ui-datepicker-year']")

        date_list = self.driver.find_elements(by=By.XPATH,value="//table[@class='ui-datepicker-calendar']//a")

        # while month.text != "September" and year.text != "2023":
        #     next_button.click()
        #     break
        


        for date in date_list:
            data = date.text
            print(date)
            if data == '12':
                date.click()
                break



    def select_menu(self):
        """ This method is to perform all the dropdown/select operations 
        based on select_by_visible_text ; select_by_index etc """

        self.open_webpage()

        select_speed = self.driver.find_element(by=By.ID,value="speed")
        speed = Select(select_speed)
        speed.select_by_visible_text("Medium")
        time.sleep(1)

        select_file = self.driver.find_element(by=By.ID,value="files")
        drop_down = Select(select_file)
        drop_down.select_by_value("3")
        time.sleep(1)

        select_num = self.driver.find_element(by=By.ID,value="number")
        drop_down_2 = Select(select_num)
        drop_down_2.select_by_visible_text("3")
        time.sleep(1)

        select_product = self.driver.find_element(by=By.ID,value="products")
        drop_down_3 = Select(select_product)
        drop_down_3.select_by_value("Microsoft")
        time.sleep(1)

        select_animal = self.driver.find_element(by=By.ID,value="animals")
        drop_down_4 = Select(select_animal)
        drop_down_4.select_by_value("avatar")
        time.sleep(1)



    def sign_up_page(self):
        """ This method is to fill the form by sending text,
        clicking on radio button, selecting the checkbox etc and submit the form """

        self.open_webpage()

        # This form is in a iframe, to continue switch_to.frame is used
        self.driver.switch_to.frame('frame-one1434677811')

        self.driver.implicitly_wait(5)
        # The above implicit wait will be applicable to all the 
        # web elements mentioned in the test script below

        first_name = self.driver.find_element(by=By.ID,value="RESULT_TextField-1")
        first_name.send_keys("santosh")
        time.sleep(1)

        last_name = self.driver.find_element(by=By.ID,value="RESULT_TextField-2")
        last_name.send_keys("kumar")
        time.sleep(1)

        phone = self.driver.find_element(by=By.ID,value="RESULT_TextField-3")
        phone.send_keys("1234567890")
        time.sleep(1)

        country = self.driver.find_element(by=By.ID,value="RESULT_TextField-4")
        country.send_keys("India")
        time.sleep(1)

        city = self.driver.find_element(by=By.ID,value="RESULT_TextField-5")
        city.send_keys("Vizag")
        time.sleep(1)

        email = self.driver.find_element(by=By.ID,value="RESULT_TextField-6")
        email.send_keys("santosh@gmail.com")
        time.sleep(1)

        male = self.driver.find_element(by=By.XPATH,value="//label[@for='RESULT_RadioButton-7_0']")
        
        """
        selenium.common.exceptions.ElementClickInterceptedException: Message: 
        Element <input id="RESULT_CheckBox-8_1" class="multiple_choice" name="RESULT_CheckBox-8" type="checkbox"> 
        is not clickable at point (29,884) because another element <label> obscures it
        """

        self.driver.execute_script("arguments[0].scrollIntoView();",male)
        time.sleep(2)

        self.driver.execute_script("arguments[0].click();",male)

        time.sleep(1)

        monday = self.driver.find_element(by=By.ID,value="RESULT_CheckBox-8_1")
        self.driver.execute_script("arguments[0].click();",monday)
        time.sleep(1)

        tuesday = self.driver.find_element(by=By.ID,value="RESULT_CheckBox-8_2")
        self.driver.execute_script("arguments[0].click();",tuesday)
        time.sleep(1)

        thursday = self.driver.find_element(by=By.ID,value="RESULT_CheckBox-8_4")
        self.driver.execute_script("arguments[0].click();",thursday)
        time.sleep(1)

        time_to_contact = self.driver.find_element(by=By.ID,value="RESULT_RadioButton-9")
        select_option = Select(time_to_contact)
        select_option.select_by_value("Radio-1")
        time.sleep(1)

        # file_upload_button = self.driver.find_element(by=By.ID,value="RESULT_FileUpload-10")

        final_submit_form = self.driver.find_element(by=By.ID,value="FSsubmit")
        self.driver.execute_script("arguments[0].click();",final_submit_form)
        time.sleep(2)



    def double_click(self):
        """ This method is to perform double click operation 
        on the button so that the """

        self.open_webpage()

        action = ActionChains(self.driver)

        copy_button = self.driver.find_element(by=By.XPATH,value="//button[normalize-space()='Copy Text']")

        # Here by using double_click method the button will be pressed 
        action.double_click(copy_button).perform()

        time.sleep(2)

        self.close_webpage()



    def drag_drop(self):
        
        self.open_webpage()

        action = ActionChains(self.driver)

        source_1 = self.driver.find_element(by=By.ID,value="draggable")
        target_1 = self.driver.find_element(by=By.ID,value="droppable")

        """ The below line is to scroll till the source_1 webelement """
        self.driver.execute_script("arguments[0].scrollIntoView();",source_1)
        time.sleep(2)

        action.drag_and_drop(source_1,target_1).perform()

        time.sleep(2)

        self.close_webpage()



    def drag_drop_image(self):
        """ here image is dragged and dropped from source to destination """

        self.open_webpage()

        action = ActionChains(self.driver)

        source_2 = self.driver.find_element(by=By.XPATH,value="//h5[normalize-space()='Mr John']")
        target_2 = self.driver.find_element(by=By.ID,value="trash")

        """ The below line is to scroll till the webelement """
        self.driver.execute_script("arguments[0].scrollIntoView();",source_2)
        time.sleep(2)

        action.drag_and_drop(source_2,target_2).perform()

        # action.click_and_hold(source_2).move_to_element(target_2).pause(2).move_by_offset(1165,148).release().perform()

        time.sleep(2)

        print(" Mr.John is moved to trash .... ")

        self.close_webpage()



    def slider(self):
        """ Here slide operation is performed on the slider """

        self.open_webpage()

        action = ActionChains(self.driver)

        slider = self.driver.find_element(by=By.XPATH,value="//h2[normalize-space()='Slider']")

        """ The below line is to scroll till the SLIDER heading in the webpage 
        using javascript argument in the execute_script method
        """
        self.driver.execute_script("arguments[0].scrollIntoView();",slider)
        time.sleep(2)

        """ Taking screenshot before the sliding operation """
        self.driver.save_screenshot('Screenshot_' + str(random.randint(0,100)) + '.png')

        slider_bar = self.driver.find_element(by=By.XPATH,value="//span[@class='ui-slider-handle ui-corner-all ui-state-default']")

        # Here it will drag till x-offset of value 50
        action.drag_and_drop_by_offset(slider_bar,50,0).perform()

        time.sleep(2)

        """ Taking screenshot after the sliding operation """
        self.driver.save_screenshot('Screenshot_after_'+ str(random.randint(0,100)) +'.png')

        self.close_webpage()


    #    
    def table_access(self):
        """ HTML Table operations like
        no. of rows, no. of columns, printing the entire data from the table
        """

        self.open_webpage()

        html_table = self.driver.find_element(by=By.XPATH,value="//h2[normalize-space()='HTML Table']")

        html_table.location_once_scrolled_into_view

        time.sleep(2)

        row_num = len(self.driver.find_elements(by=By.XPATH,value='//*[@id="HTML1"]/div[1]/table/tbody/tr'))

        col_num = len(self.driver.find_elements(by=By.XPATH,value="//table[@name='BookTable']//tr[2]//td"))

        print("Number of ROWS in the table are : ",row_num)

        print("Number of COLOUMNS in the table are : ",col_num)

        time.sleep(2)
        

        """ To print the entire data from the table """
        before_xpath = "//table[@name='BookTable']//tbody//tr["
        aftertd_xpath = "]//td["
        aftertr_xpath = "]"

        for t_row in range(2,(row_num + 1)):
            for t_col in range(1,(col_num + 1)):
                final_xpath = before_xpath + str(t_row) + aftertd_xpath + str(t_col) + aftertr_xpath
                cell_text = self.driver.find_element(by=By.XPATH, value = final_xpath).text
                #print(cell_text,end=" ")
                print(cell_text)
            print()

        self.close_webpage()



    def tool_tip(self):
        """ Performed mouse hover on the webelement for tooltip action """

        self.open_webpage()

        action = ActionChains(self.driver)

        heading = self.driver.find_element(by=By.XPATH,value="//h2[normalize-space()='Tooltips']")
        heading.location_once_scrolled_into_view

        hover = self.driver.find_element(by=By.ID,value="age")
        action.move_to_element(hover).perform()
        # hover.click()
        time.sleep(2)

        self.close_webpage()

    
    #
    def resizable(self):

        self.open_webpage()

        action = ActionChains(self.driver)

        heading = self.driver.find_element(by=By.XPATH,value="//h2[normalize-space()='Resizable']")

        heading.location_once_scrolled_into_view

        time.sleep(1)

        draggable = self.driver.find_element(by=By.XPATH,value="//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")

        action.drag_and_drop_by_offset(draggable,1100,250).perform()

    

    def text_label(self):

        self.open_webpage()

        label_text = self.driver.find_element(by=By.ID,value="Text1").text

        print(label_text)



    def text_print_full_page(self):
        """ In this method we will print the entier text from the webpage """

        self.open_webpage()

        full_page = self.driver.find_element(by=By.TAG_NAME,value="body").text

        print(full_page)

        self.close_webpage()



    def close_webpage(self):
        """ close the webdriver/window """

        self.driver.close()



s = automation()

s.slider()

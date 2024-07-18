from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image
#import pytesseract

driver = webdriver.Chrome()
driver.get("https://testffc.nimapinfotech.com/auth/login")

username = "someshmaslekar@gmail.com"
password = "Somesh@29"

customerNameValue = "somesh"
refNoValue = "abcdefgh"
contachPersonNameValue = "XYZ"
mobileNumberValue = "9999999999"
telephoneNumberValue = "0202020202"
emailValue = "abc@xyz.com"
contactPersonDesignationValue = "CEO"
AddressValue = "lorem ipsum"
countryValue = "India"
def signIn(username, password):
    user_ = driver.find_element(By.ID, "mat-input-0")
    pass_ = driver.find_element(By.ID, "mat-input-1")
    signInButton = driver.find_element(By.ID, "kt_login_signin_submit")
    user_.send_keys(username)
    pass_.send_keys(password)
    signInButton.click()
    # canvas = driver.find_element(By.XPATH, "/html/body/kt-auth/div/div/div[2]/kt-login/div[2]/div/form/div[3]/kt-captcha/div/canvas")
    # canvas.screenshot_as_png('img.png')

def verifyToast():
    while True:
        try:
            punchInButton = driver.find_element(By.XPATH, "/html/body/kt-base/div[2]/div/div/kt-header/div/kt-topbar/div/kt-user-punch/div/div[2]/button/span")
            punchInButton.click();
            toastContainer = driver.find_element(By.ID, "toast-container")
            toastMessage = toastContainer.text
            print("Toast Message is ")
            print(toastMessage)
            time.sleep(2)
            # if toastMessage!="": 
            return
        except:
            pass

def addCustomer():
    while True:
        try:
           
            MyCustomerButtonRef = driver.find_element(By.XPATH, "/html/body/kt-base/div[2]/div/kt-aside-left/div/div/div/ul/li[2]/a/span")
            MyCustomerButtonRef.click();
            newCustomerbutton = driver.find_element(By.XPATH, "/html/body/kt-base/div[2]/div/div/div/div/ng-component/kt-customers-list/mat-drawer-container/mat-drawer-content/kt-portlet/div/kt-portlet-header/div[4]/button[1]/span")
            newCustomerbutton.click();
            time.sleep(2)

            customerNameElement = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/kt-customers-edit-dialog/div[1]/form/div/div[2]/div[1]/mat-form-field/div/div[1]/div/input")
            customerNameElement.send_keys(customerNameValue)

            refNoElement = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/kt-customers-edit-dialog/div[1]/form/div/div[2]/div[2]/mat-form-field/div/div[1]/div/input")
            refNoElement.send_keys(refNoValue)

            contachPersonNameElement = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/kt-customers-edit-dialog/div[1]/form/div/div[4]/div[1]/mat-form-field/div/div[1]/div/input")
            contachPersonNameElement.send_keys(contachPersonNameValue)

            mobileNumberElement = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/kt-customers-edit-dialog/div[1]/form/div/div[4]/div[2]/mat-form-field/div/div[1]/div/input")
            mobileNumberElement.send_keys(mobileNumberValue)

            telephoneNumberElement = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/kt-customers-edit-dialog/div[1]/form/div/div[4]/div[3]/mat-form-field/div/div[1]/div/input")
            telephoneNumberElement.send_keys(telephoneNumberValue)

            emailElement = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/kt-customers-edit-dialog/div[1]/form/div/div[4]/div[4]/mat-form-field/div/div[1]/div/input")
            emailElement.send_keys(emailValue)

            contactPersonDesignationElement = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/kt-customers-edit-dialog/div[1]/form/div/div[4]/div[5]/mat-form-field/div/div[1]/div/input")
            contactPersonDesignationElement.send_keys(contactPersonDesignationValue)

            AddressElement = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/kt-customers-edit-dialog/div[1]/form/div/div[6]/div[1]/mat-form-field/div/div[1]/div")
            AddressElement.click()

            doneElement = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div/mat-dialog-container/kt-address-dialog/kt-portlet/div/kt-portlet-body/div[2]/button")
            doneElement.click()

            countryElement = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/kt-customers-edit-dialog/div[1]/form/div/div[6]/div[2]/mat-form-field/div/div[1]/div")
            countryElement.click()

            # countrySearchElement = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/mat-dialog-container/kt-customers-edit-dialog/div[1]/form/div/div[6]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]")
            # countrySearchElement.click()
            # countryInputElement = driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/div/div[1]/mat-form-field/div/div[1]/div/input")
            # countryInputElement.send_keys(countryValue)

            return
        except:
            pass

signIn(username, password)
verifyToast()
addCustomer()

time.sleep(30)
driver.quit()














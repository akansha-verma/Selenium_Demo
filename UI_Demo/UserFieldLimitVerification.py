username = browser.find_element_by_id("systemUser_userName")
username.send_keys("abhidixitabhidixitabhidixitabhidixitabh" + str(randomInt))
#Verify the MaxLength of UserName Field
EnteredValue = username.get_attribute("value")
EnteredValueSize=len(str(EnteredValue))
print(EnteredValueSize)
if EnteredValueSize == 40:
    print('Maxlength character functionality is 40 and its working fine.')
else:
    print('It allow more than 40')


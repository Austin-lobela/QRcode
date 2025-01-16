#aUSTINS
import qrcode

def create_website_qr():
    url = input("Enter the website URL: ")
    qr = qrcode.make(url)
    qr.show()

def create_contact_qr():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number: ")
    website_url = input("Enter your website URL (optional): ")
    social_media_code = input("Enter your social media code (optional): ")
    
    # Create the vCard format string
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name} {surname}\nTEL:{phone_number}\nEMAIL:{email}\nURL:{website_url}\nX-SOCIALPROFILE:{social_media_code}\nEND:VCARD"
    
    # Create QR code with vCard
    qr = qrcode.make(vcard)
    qr.show()

def create_social_media_qr():
    social_media_link = input("Enter the social media link: ")
    qr = qrcode.make(social_media_link)
    qr.show()

def main():
    print("Choose an option:")
    print("a. Website")
    print("b. Contact Number")
    print("c. Social Media")
    
    choice = input("Enter your choice (a/b/c): ").strip().lower()
    
    if choice == 'a':
        create_website_qr()
    elif choice == 'b':
        create_contact_qr()
    elif choice == 'c':
        create_social_media_qr()
    else:
        print("Invalid choice. Please select a, b, or c.")

if __name__ == "__main__":
    main()
    
    

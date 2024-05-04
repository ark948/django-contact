from contacts.models import ContactEntry

def make_new_contact_entry(title, **kwargs):
    try:
        new_contact = ContactEntry()
        new_contact.title = title
        if 'first_name' in  kwargs:
            new_contact.first_name = kwargs["first_name"]
        elif 'last_name' in kwargs:
            new_contact.last_name = kwargs["last_name"]
        elif 'phone_number' in kwargs:
            new_contact.phone_number = kwargs["phone_number"]
        elif 'email' in kwargs:
            new_contact.email = kwargs["email"]
        elif 'address' in kwargs:
            new_contact.address = kwargs["address"]
        try:
            new_contact.save()
            return new_contact.__str__
        except Exception as inner_error:
            print(inner_error)
            return None
    except Exception as outer_error:
        print(outer_error)
        return None

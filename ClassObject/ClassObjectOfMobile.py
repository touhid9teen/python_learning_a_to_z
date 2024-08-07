# -----------Task-1-----------

# একটা মোবাইল ক্লাস বানান , যেখানে আমরা কত মেগাপিক্সেল ক্যামেরা আছে
#  , ডিসপ্লে সাইজ কত , র‍্যাম কত , রম কত , এই তথ্য গুলা আলাদা ভাবে
#  জানতে পারবো এবং এর স্ট্রিং রিপ্রেজেন্টেশনে এর ব্রান্ড নেম এবং মডেল 
# নেম সহ দেখাবে । যেমন ঃ Samsung – brand name ;
#  S21 – model name -> তাহলে রিপ্রেজেন্টেশনে দেখাবে “Samsung S21”


class Mobile:
    def __init__ (self, band, modle, camera, displaySize, ram, rom):

#__init__ একটা স্পেশাল মেথড যা ক্লাস তৈরি হলে অটোমেটিক কল হয় 
#এই মেথড এর মাধ্যমে আমরা ক্লাস এর অবজেক্ট তৈরি করতে পারি
#self একটা প্যারামিটার যা ক্লাস এর অবজেক্ট তৈরি করতে হলে
#  অবশ্যই থাকতে হবে
#self is a reference to the current instance of the class.
# It is used to access variables that belongs to the class.
# It is used to access methods that belongs to the class.

        self.band_name = band
        self.modle_name = modle
        self.camera_name = camera
        self.display_Size = displaySize
        self.ram_is = ram
        self.rom_is = rom

    def __str__ (self):
        return f"{self.band_name} {self.modle_name}"
    
# __str__ একটা স্পেশাল মেথড যা ক্লাস এর অবজেক্ট 
# কে স্ট্রিং এ কনভার্ট করে
#When you print an instance of the class,
#  the __str__ method is automatically called

    def camera(self):
        return self.camera_name
    def get_display(self):
        return self.display_Size
    def ram(self):
        return self.ram_is
    def rom(self):
        return self.rom_is
    
mobile1 = Mobile("Samsung", "S21", "108MP", "6.2 inch", "8GB", "128GB")

print(mobile1) 
print (mobile1.camera())
print(mobile1.get_display())
print(mobile1.ram())
print(mobile1.rom())

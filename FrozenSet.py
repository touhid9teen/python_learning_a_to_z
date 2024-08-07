fset =   frozenset([1, 2, 3, 4, 5])
print('This is \"frozenset\'s\" element :')

for i in fset:
    print(i)

try:
    fset.add(5)
except AttributeError as e:
    print(e)  
    
# Output: 'frozenset' object has no attribute 'add'

# frozenset থেকে আইটেম মুছে ফেলার চেষ্টা করা হচ্ছে
try:
    fset.remove(3)
except AttributeError as e:
    print(e)  
    
# Output: 'frozenset' object has no attribute 'remove'



#----------------Use Case-------------------

#1. যেহেতু frozenset অপরিবর্তনীয়, এটি ডিকশনারির কী (key) হিসেবে ব্যবহার করা যায়।
#2. সেটের মধ্যে সেট
# # Example of using frozenset in a set
set_of_sets = set()
set_of_sets.add(frozenset([1, 2, 3]))
set_of_sets.add(frozenset([4, 5, 6]))

print('set_of_sets') 
for i in set_of_sets:
    for j in i:
        print(j, end=' ')
    print()

#end=' 'prints each element j followed by a space instead of a newline.
#print() is used to add a newline after each inner set is printed.

#3. যখন ডেটা পরিবর্তন হওয়া থেকে রোধ করা দরকার, তখন frozenset ব্যবহার করা হয়। এটি নিশ্চিত করে যে ডেটা অপরিবর্তনীয় থাকবে।

#4. ডিফল্ট আর্গুমেন্ট হিসেবে পরিবর্তনশীল বস্তু ব্যবহার করা সাধারণত নিরাপদ নয়। frozenset এখানে একটি নিরাপদ অপশন হতে পারে।

#5. ডেটা ভ্যালিডেশন এবং সমতা যাচাই

# Example of using frozenset for data validation and equality checking
allowed_values = frozenset(["apple", "banana", "cherry"])
user_input = "apple"

if user_input in allowed_values:
    print("Valid input")
else:
    print("Invalid input")
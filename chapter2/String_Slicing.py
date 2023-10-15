# Sub-string(slicing)
name = "Hello,World";
print(name[0 : 5]); # 0 to 4 index chars, 5 is excluded from the range
print(name[ : 5]);  # python will itself put 0 before colon
print(name[1 : ]);  # python consider upto the last
print(name[ : ]);  # == name
print(name[-1 : 3]);  # length-1 : 3 (10,3)   will wont run
print(name[-7 : 8]);  # length - 7 : 8 (4,8)
print(name[-3 : -1]);  # length - 4 : length - 1 (8,9)
print(name[len(name) -3 :len(name) -1]);

# length of string len() function
print(len(name));

#Quick Quiz
str = "Happy Journey";
print(str[-4:9]);

# ans is "" blank
# len-4 => 9, so (9,9) => ""

print(str[-8:12]);
#ans is (5,11) " Journe"
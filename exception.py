# Exception handling

try:  # try this code
    print("Hello+5")

except TypeError:  # don't stop exceution and return this if error/exception happens
    print("Something went wrong. Most Likely a Type Error")

except SyntaxError:
    print("Some other error")

finally:  # execute this is any case
    print("Hey")

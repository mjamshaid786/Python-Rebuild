# show the output into single clean format
# "968-Maria, ( D@t@ Engineer ) ;; 27y  "

data = "968-Maria, ( D@t@ Engineer ) ;; 27y  "

clean_data = data.strip().replace("968-", "").replace("@", "a").replace(";", "").replace(",", "").replace("(", "").replace(")", "")
print(clean_data)
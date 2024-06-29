My 10th assignment! These were refreshing because packing and unpacking tuples was the functionality I was missing from the prior dictionary assignmemt. Knowing what I do now, I'd probably handle the prior assignment like so:
1. get category of "open tickets" from dictionary
2. get items tuple from open tickets
3. serve menu of items to user, showing the keys and values (for key, value in open_tickets: print(f"{index}. {key}{value}"))
4. be able to directly check what the key of the option chosen is and pass that along to the relevant update and get functions instead of working around the limitations of passing just an index
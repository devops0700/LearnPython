def shut_down(s="yes"):
#    s = "yes"
#    print (s)
    if s == "yes":
        print(s)
        return "Shutting down"
        print "successful"

    elif s == "no":
        return "Shutdown aborted"

    else:
        return "Sorry"

#shut_down("yes")
shut_down()
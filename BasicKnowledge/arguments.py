def print_info(*args, **kwargs):
    print("------info------")
    print(kwargs.get("Name"))
    print(kwargs.get("Age"))
    print(kwargs.get("Sex"))
    print(kwargs.get("Hobbie"))


print_info(Name="Nick", Age=24, Sex="M", Hobbie="sex")

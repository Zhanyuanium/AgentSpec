from .pythonrepl import checks

# code-domain predicates
predicate_table = {}
for id in checks:
    for check_func in checks[id]:
        predicate_table[check_func.__name__] = check_func
    
# print( "' | '".join(predicate_table.keys()))
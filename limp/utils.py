def evaluates_safely(form):
    try:
        form.evaluate()
        return True
    except:
        return False

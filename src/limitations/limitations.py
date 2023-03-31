def getInstructions():
    try:
        with open("./prompt_limitations.txt") as prompt_limit:
            indications = prompt_limit.readlines()
            prompt_limit.close()

            return {
                "status": 200,
                "indications": " ".join(indications),
            }
    except:
        return {
            "status": 400,
            "indications": None
        }
{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":234,"column":0},"end":{"row":293,"column":66},"action":"insert","lines":["@app.route(\"/filter_recipe\", methods=[\"GET\", \"POST\"])","def filter_recipe():","    \"\"\"","    Filter by difficulty level, origin, time, and serving","    \"\"\"","    ","    recipes = mongo.db.recipes # Set our collection","    criteria = [] # An array for use in the mongo query","    ","","    if request.method == \"POST\":","        origins = request.form.get('recipe_origin')","        if origins is not None:","            dict1 = {","                    'recipe_origins': origins","                    }","            criteria.append(dict1)","    ","        #time = request.form.get('recipe_time')","        #if time is not None:","            #dict2 = {","                    #'recipe_time': time","                    #}","            #criteria.append(dict2)","    ","        difficulty = request.form.get('recipe_difficulty')","        if difficulty is not None:","            dict3 = {","                    'recipe_difficulty': difficulty","                }","            criteria.append(dict3)","            ","        #serving = request.form.get('recipe_serving')","        #if serving is not None:","            #dict4 = {","                    #'recipe_serving' : serving","                #}","            #criteria.append(dict4)","        results = recipes.find({'$and': criteria })","        count = recipes.find({'$and': criteria }).count()","        print(count)","        print(criteria)","        for r in result:","            print(r)","        return render_template(\"filter_recipe.html\", #results=results,","                                origins=mongo.db.origins.find(),","                                time=mongo.db.time.find(),","                                serving=mongo.db.serving.find(),","                                difficulty=mongo.db.difficulty.find())","","    ","","        ","    ","    ","    return render_template(\"filter_recipe.html\",","                            origins=mongo.db.origins.find(),","                            time=mongo.db.time.find(),","                            serving=mongo.db.serving.find(),","                            difficulty=mongo.db.difficulty.find())"],"id":3394}],[{"start":{"row":276,"column":23},"end":{"row":276,"column":24},"action":"insert","lines":["s"],"id":3395}],[{"start":{"row":234,"column":0},"end":{"row":293,"column":66},"action":"remove","lines":["@app.route(\"/filter_recipe\", methods=[\"GET\", \"POST\"])","def filter_recipe():","    \"\"\"","    Filter by difficulty level, origin, time, and serving","    \"\"\"","    ","    recipes = mongo.db.recipes # Set our collection","    criteria = [] # An array for use in the mongo query","    ","","    if request.method == \"POST\":","        origins = request.form.get('recipe_origin')","        if origins is not None:","            dict1 = {","                    'recipe_origins': origins","                    }","            criteria.append(dict1)","    ","        #time = request.form.get('recipe_time')","        #if time is not None:","            #dict2 = {","                    #'recipe_time': time","                    #}","            #criteria.append(dict2)","    ","        difficulty = request.form.get('recipe_difficulty')","        if difficulty is not None:","            dict3 = {","                    'recipe_difficulty': difficulty","                }","            criteria.append(dict3)","            ","        #serving = request.form.get('recipe_serving')","        #if serving is not None:","            #dict4 = {","                    #'recipe_serving' : serving","                #}","            #criteria.append(dict4)","        results = recipes.find({'$and': criteria })","        count = recipes.find({'$and': criteria }).count()","        print(count)","        print(criteria)","        for r in results:","            print(r)","        return render_template(\"filter_recipe.html\", #results=results,","                                origins=mongo.db.origins.find(),","                                time=mongo.db.time.find(),","                                serving=mongo.db.serving.find(),","                                difficulty=mongo.db.difficulty.find())","","    ","","        ","    ","    ","    return render_template(\"filter_recipe.html\",","                            origins=mongo.db.origins.find(),","                            time=mongo.db.time.find(),","                            serving=mongo.db.serving.find(),","                            difficulty=mongo.db.difficulty.find())"],"id":3396}],[{"start":{"row":234,"column":0},"end":{"row":282,"column":70},"action":"insert","lines":["@app.route(\"/filter_recipe\", methods=[\"GET\", \"POST\"])","def filter_recipe():","    \"\"\"","    Filter by difficulty level, origin, time, and serving","    \"\"\"","    ","    recipes = mongo.db.recipes # Set our collection","    criteria = [] # An array for use in the mongo query","    ","","    if request.method == \"POST\":","        origins = request.form.get('recipe_origin')","        if origins is not None:","            dict1 = {","                    'recipe_origins': origins","                    }","            criteria.append(dict1)","    ","        #time = request.form.get('recipe_time')","        #if time is not None:","            #dict2 = {","                    #'recipe_time': time","                    #}","            #criteria.append(dict2)","    ","        difficulty = request.form.get('recipe_difficulty')","        if difficulty is not None:","            dict3 = {","                    'recipe_difficulty': difficulty","                }","            criteria.append(dict3)","            ","        #serving = request.form.get('recipe_serving')","        #if serving is not None:","            #dict4 = {","                    #'recipe_serving' : serving","                #}","            #criteria.append(dict4)","        results = recipes.find({'$and': [{‘recipe_origins’: u’Japanese’}, {‘recipe_difficulty’: u’Hard’}] })","        count = results.count","        print(count)","        print(criteria)","        for r in result:","            print(r)","        return render_template(\"filter_recipe.html\", #results=results,","                                origins=mongo.db.origins.find(),","                                time=mongo.db.time.find(),","                                serving=mongo.db.serving.find(),","                                difficulty=mongo.db.difficulty.find())"],"id":3397}],[{"start":{"row":276,"column":23},"end":{"row":276,"column":24},"action":"insert","lines":["s"],"id":3398}],[{"start":{"row":272,"column":42},"end":{"row":272,"column":43},"action":"remove","lines":["‘"],"id":3399}],[{"start":{"row":272,"column":42},"end":{"row":272,"column":43},"action":"insert","lines":["'"],"id":3400}],[{"start":{"row":272,"column":57},"end":{"row":272,"column":58},"action":"remove","lines":["’"],"id":3401}],[{"start":{"row":272,"column":57},"end":{"row":272,"column":58},"action":"insert","lines":["'"],"id":3402}],[{"start":{"row":272,"column":62},"end":{"row":272,"column":63},"action":"insert","lines":["'"],"id":3403}],[{"start":{"row":272,"column":62},"end":{"row":272,"column":63},"action":"remove","lines":["'"],"id":3404},{"start":{"row":272,"column":61},"end":{"row":272,"column":62},"action":"remove","lines":["’"]}],[{"start":{"row":272,"column":61},"end":{"row":272,"column":62},"action":"insert","lines":["'"],"id":3405}],[{"start":{"row":272,"column":70},"end":{"row":272,"column":71},"action":"remove","lines":["’"],"id":3406}],[{"start":{"row":272,"column":70},"end":{"row":272,"column":71},"action":"insert","lines":["'"],"id":3407}],[{"start":{"row":272,"column":75},"end":{"row":272,"column":76},"action":"remove","lines":["‘"],"id":3408}],[{"start":{"row":272,"column":75},"end":{"row":272,"column":76},"action":"insert","lines":["'"],"id":3409}],[{"start":{"row":272,"column":93},"end":{"row":272,"column":94},"action":"remove","lines":["’"],"id":3410}],[{"start":{"row":272,"column":93},"end":{"row":272,"column":94},"action":"insert","lines":["'"],"id":3411}],[{"start":{"row":272,"column":97},"end":{"row":272,"column":98},"action":"remove","lines":["’"],"id":3412}],[{"start":{"row":272,"column":97},"end":{"row":272,"column":98},"action":"insert","lines":["'"],"id":3413}],[{"start":{"row":272,"column":102},"end":{"row":272,"column":103},"action":"remove","lines":["’"],"id":3414}],[{"start":{"row":272,"column":102},"end":{"row":272,"column":103},"action":"insert","lines":["'"],"id":3415}],[{"start":{"row":234,"column":0},"end":{"row":282,"column":70},"action":"remove","lines":["@app.route(\"/filter_recipe\", methods=[\"GET\", \"POST\"])","def filter_recipe():","    \"\"\"","    Filter by difficulty level, origin, time, and serving","    \"\"\"","    ","    recipes = mongo.db.recipes # Set our collection","    criteria = [] # An array for use in the mongo query","    ","","    if request.method == \"POST\":","        origins = request.form.get('recipe_origin')","        if origins is not None:","            dict1 = {","                    'recipe_origins': origins","                    }","            criteria.append(dict1)","    ","        #time = request.form.get('recipe_time')","        #if time is not None:","            #dict2 = {","                    #'recipe_time': time","                    #}","            #criteria.append(dict2)","    ","        difficulty = request.form.get('recipe_difficulty')","        if difficulty is not None:","            dict3 = {","                    'recipe_difficulty': difficulty","                }","            criteria.append(dict3)","            ","        #serving = request.form.get('recipe_serving')","        #if serving is not None:","            #dict4 = {","                    #'recipe_serving' : serving","                #}","            #criteria.append(dict4)","        results = recipes.find({'$and': [{'recipe_origins': u'Japanese'}, {'recipe_difficulty': u'Hard'}] })","        count = results.count","        print(count)","        print(criteria)","        for r in results:","            print(r)","        return render_template(\"filter_recipe.html\", #results=results,","                                origins=mongo.db.origins.find(),","                                time=mongo.db.time.find(),","                                serving=mongo.db.serving.find(),","                                difficulty=mongo.db.difficulty.find())"],"id":3416}],[{"start":{"row":234,"column":0},"end":{"row":276,"column":49},"action":"insert","lines":["@app.route(\"/filter_recipe\", methods=[\"GET\", \"POST\"])","def filter_recipe():","    \"\"\"","    Filter by difficulty level, origin, time, and serving","    \"\"\"","    ","    recipes = mongo.db.recipes # Set our collection","    criteria = [] # An array for use in the mongo query","    ","    if request.method == \"POST\":","        origins = request.form.get('recipe_origin')","        if origins is not None:","            dict1 = {","                    'recipe_origin': origins","                    }","            criteria.append(dict1)","    ","        #time = request.form.get('recipe_time')","        #if time is not None:","            #dict2 = {","                    #'recipe_time': time","                    #}","            #criteria.append(dict2)","    ","        difficulty = request.form.get('recipe_difficulty')","        if difficulty is not None:","            dict3 = {","                    'recipe_difficulty': difficulty","                }","            criteria.append(dict3)","            ","        #serving = request.form.get('recipe_serving')","        #if serving is not None:","            #dict4 = {","                    #'recipe_serving' : serving","                #}","            #criteria.append(dict4)","        ","        results = recipes.find({'$and': criteria })","","        return render_template(\"filter_recipe.html\", results=results)","    ","    return render_template(\"filter_recipe.html\",)"],"id":3417}],[{"start":{"row":274,"column":68},"end":{"row":274,"column":69},"action":"insert","lines":[","],"id":3418}],[{"start":{"row":274,"column":69},"end":{"row":275,"column":0},"action":"insert","lines":["",""],"id":3419},{"start":{"row":275,"column":0},"end":{"row":275,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":275,"column":8},"end":{"row":275,"column":12},"action":"insert","lines":["    "],"id":3420}],[{"start":{"row":275,"column":12},"end":{"row":275,"column":16},"action":"insert","lines":["    "],"id":3421}],[{"start":{"row":275,"column":16},"end":{"row":275,"column":20},"action":"insert","lines":["    "],"id":3422}],[{"start":{"row":275,"column":20},"end":{"row":275,"column":24},"action":"insert","lines":["    "],"id":3423}],[{"start":{"row":275,"column":24},"end":{"row":275,"column":28},"action":"insert","lines":["    "],"id":3424}],[{"start":{"row":275,"column":28},"end":{"row":275,"column":32},"action":"insert","lines":["    "],"id":3425}],[{"start":{"row":275,"column":32},"end":{"row":278,"column":65},"action":"insert","lines":["origins=mongo.db.origins.find(),","                            time=mongo.db.time.find(),","                            serving=mongo.db.serving.find(),","                            difficulty=mongo.db.difficulty.find()"],"id":3426}],[{"start":{"row":275,"column":28},"end":{"row":275,"column":32},"action":"remove","lines":["    "],"id":3427}],[{"start":{"row":275,"column":60},"end":{"row":277,"column":60},"action":"remove","lines":["","                            time=mongo.db.time.find(),","                            serving=mongo.db.serving.find(),"],"id":3444}],[{"start":{"row":275,"column":28},"end":{"row":276,"column":65},"action":"remove","lines":["origins=mongo.db.origins.find(),","                            difficulty=mongo.db.difficulty.find()"],"id":3445}],[{"start":{"row":275,"column":24},"end":{"row":275,"column":28},"action":"remove","lines":["    "],"id":3446},{"start":{"row":275,"column":20},"end":{"row":275,"column":24},"action":"remove","lines":["    "]},{"start":{"row":275,"column":16},"end":{"row":275,"column":20},"action":"remove","lines":["    "]},{"start":{"row":275,"column":12},"end":{"row":275,"column":16},"action":"remove","lines":["    "]},{"start":{"row":275,"column":8},"end":{"row":275,"column":12},"action":"remove","lines":["    "]},{"start":{"row":275,"column":4},"end":{"row":275,"column":8},"action":"remove","lines":["    "]},{"start":{"row":275,"column":0},"end":{"row":275,"column":4},"action":"remove","lines":["    "]},{"start":{"row":274,"column":69},"end":{"row":275,"column":0},"action":"remove","lines":["",""]},{"start":{"row":274,"column":68},"end":{"row":274,"column":69},"action":"remove","lines":[","]}],[{"start":{"row":276,"column":48},"end":{"row":277,"column":0},"action":"insert","lines":["",""],"id":3447},{"start":{"row":277,"column":0},"end":{"row":277,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":277,"column":4},"end":{"row":277,"column":8},"action":"insert","lines":["    "],"id":3448}],[{"start":{"row":277,"column":8},"end":{"row":277,"column":12},"action":"insert","lines":["    "],"id":3449}],[{"start":{"row":277,"column":12},"end":{"row":277,"column":16},"action":"insert","lines":["    "],"id":3450}],[{"start":{"row":277,"column":16},"end":{"row":277,"column":20},"action":"insert","lines":["    "],"id":3451}],[{"start":{"row":277,"column":20},"end":{"row":277,"column":24},"action":"insert","lines":["    "],"id":3452}],[{"start":{"row":277,"column":24},"end":{"row":277,"column":28},"action":"insert","lines":["    "],"id":3453}],[{"start":{"row":277,"column":24},"end":{"row":277,"column":28},"action":"remove","lines":["    "],"id":3454}],[{"start":{"row":277,"column":24},"end":{"row":278,"column":65},"action":"insert","lines":["origins=mongo.db.origins.find(),","                            difficulty=mongo.db.difficulty.find()"],"id":3455}],[{"start":{"row":278,"column":24},"end":{"row":278,"column":28},"action":"remove","lines":["    "],"id":3456}],[{"start":{"row":278,"column":62},"end":{"row":279,"column":0},"action":"insert","lines":["",""],"id":3457},{"start":{"row":279,"column":0},"end":{"row":279,"column":24},"action":"insert","lines":["                        "]}],[{"start":{"row":279,"column":20},"end":{"row":279,"column":24},"action":"remove","lines":["    "],"id":3458},{"start":{"row":279,"column":16},"end":{"row":279,"column":20},"action":"remove","lines":["    "]},{"start":{"row":279,"column":12},"end":{"row":279,"column":16},"action":"remove","lines":["    "]},{"start":{"row":279,"column":8},"end":{"row":279,"column":12},"action":"remove","lines":["    "]},{"start":{"row":279,"column":4},"end":{"row":279,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":279,"column":4},"end":{"row":280,"column":0},"action":"insert","lines":["",""],"id":3459},{"start":{"row":280,"column":0},"end":{"row":280,"column":4},"action":"insert","lines":["    "]},{"start":{"row":280,"column":4},"end":{"row":280,"column":5},"action":"insert","lines":["p"]},{"start":{"row":280,"column":5},"end":{"row":280,"column":6},"action":"insert","lines":["r"]},{"start":{"row":280,"column":6},"end":{"row":280,"column":7},"action":"insert","lines":["i"]},{"start":{"row":280,"column":7},"end":{"row":280,"column":8},"action":"insert","lines":["n"]},{"start":{"row":280,"column":8},"end":{"row":280,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":280,"column":9},"end":{"row":280,"column":11},"action":"insert","lines":["()"],"id":3460}],[{"start":{"row":280,"column":10},"end":{"row":280,"column":11},"action":"insert","lines":["c"],"id":3461},{"start":{"row":280,"column":11},"end":{"row":280,"column":12},"action":"insert","lines":["r"]},{"start":{"row":280,"column":12},"end":{"row":280,"column":13},"action":"insert","lines":["i"]},{"start":{"row":280,"column":13},"end":{"row":280,"column":14},"action":"insert","lines":["t"]},{"start":{"row":280,"column":14},"end":{"row":280,"column":15},"action":"insert","lines":["e"]},{"start":{"row":280,"column":15},"end":{"row":280,"column":16},"action":"insert","lines":["r"]},{"start":{"row":280,"column":16},"end":{"row":280,"column":17},"action":"insert","lines":["i"]},{"start":{"row":280,"column":17},"end":{"row":280,"column":18},"action":"insert","lines":["a"]}],[{"start":{"row":280,"column":4},"end":{"row":280,"column":19},"action":"remove","lines":["print(criteria)"],"id":3462}],[{"start":{"row":280,"column":0},"end":{"row":280,"column":4},"action":"remove","lines":["    "],"id":3463},{"start":{"row":279,"column":4},"end":{"row":280,"column":0},"action":"remove","lines":["",""]},{"start":{"row":279,"column":0},"end":{"row":279,"column":4},"action":"remove","lines":["    "]},{"start":{"row":278,"column":62},"end":{"row":279,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":274,"column":69},"end":{"row":275,"column":0},"action":"insert","lines":["",""],"id":3464},{"start":{"row":275,"column":0},"end":{"row":275,"column":8},"action":"insert","lines":["        "]},{"start":{"row":275,"column":8},"end":{"row":276,"column":0},"action":"insert","lines":["",""]},{"start":{"row":276,"column":0},"end":{"row":276,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":276,"column":8},"end":{"row":276,"column":23},"action":"insert","lines":["print(criteria)"],"id":3465}],[{"start":{"row":25,"column":57},"end":{"row":25,"column":58},"action":"remove","lines":["-"],"id":3466}],[{"start":{"row":251,"column":8},"end":{"row":251,"column":9},"action":"remove","lines":["#"],"id":3467}],[{"start":{"row":252,"column":8},"end":{"row":252,"column":9},"action":"remove","lines":["#"],"id":3468}],[{"start":{"row":253,"column":12},"end":{"row":253,"column":13},"action":"remove","lines":["#"],"id":3469}],[{"start":{"row":256,"column":12},"end":{"row":256,"column":13},"action":"remove","lines":["#"],"id":3470}],[{"start":{"row":265,"column":8},"end":{"row":265,"column":9},"action":"remove","lines":["#"],"id":3471}],[{"start":{"row":266,"column":8},"end":{"row":266,"column":9},"action":"remove","lines":["#"],"id":3472}],[{"start":{"row":267,"column":12},"end":{"row":267,"column":13},"action":"remove","lines":["#"],"id":3473}],[{"start":{"row":268,"column":20},"end":{"row":268,"column":21},"action":"remove","lines":["#"],"id":3474}],[{"start":{"row":269,"column":16},"end":{"row":269,"column":17},"action":"remove","lines":["#"],"id":3475}],[{"start":{"row":255,"column":20},"end":{"row":255,"column":21},"action":"remove","lines":["#"],"id":3476}],[{"start":{"row":254,"column":20},"end":{"row":254,"column":21},"action":"remove","lines":["#"],"id":3477}],[{"start":{"row":270,"column":12},"end":{"row":270,"column":13},"action":"remove","lines":["#"],"id":3478}],[{"start":{"row":290,"column":19},"end":{"row":291,"column":0},"action":"insert","lines":["",""],"id":3479},{"start":{"row":291,"column":0},"end":{"row":291,"column":8},"action":"insert","lines":["        "]},{"start":{"row":291,"column":8},"end":{"row":292,"column":0},"action":"insert","lines":["",""]},{"start":{"row":292,"column":0},"end":{"row":292,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":292,"column":4},"end":{"row":292,"column":8},"action":"remove","lines":["    "],"id":3480},{"start":{"row":292,"column":0},"end":{"row":292,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":291,"column":4},"end":{"row":292,"column":0},"action":"insert","lines":["",""],"id":3481},{"start":{"row":292,"column":0},"end":{"row":292,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":292,"column":0},"end":{"row":292,"column":4},"action":"remove","lines":["    "],"id":3482}],[{"start":{"row":292,"column":4},"end":{"row":293,"column":0},"action":"remove","lines":["",""],"id":3483},{"start":{"row":292,"column":0},"end":{"row":292,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":292,"column":0},"end":{"row":292,"column":73},"action":"insert","lines":["#=======================================================================#"],"id":3485}],[{"start":{"row":292,"column":73},"end":{"row":293,"column":0},"action":"insert","lines":["",""],"id":3486},{"start":{"row":293,"column":0},"end":{"row":294,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":294,"column":0},"end":{"row":294,"column":112},"action":"insert","lines":["\"\"\"Set up our IP address and our port number so that Cloud9 knows how to run and where to run our application\"\"\""],"id":3487}],[{"start":{"row":294,"column":4},"end":{"row":294,"column":109},"action":"remove","lines":["et up our IP address and our port number so that Cloud9 knows how to run and where to run our application"],"id":3490},{"start":{"row":294,"column":3},"end":{"row":294,"column":4},"action":"remove","lines":["S"]}],[{"start":{"row":294,"column":3},"end":{"row":294,"column":4},"action":"insert","lines":["R"],"id":3491},{"start":{"row":294,"column":4},"end":{"row":294,"column":5},"action":"insert","lines":["e"]},{"start":{"row":294,"column":5},"end":{"row":294,"column":6},"action":"insert","lines":["s"]},{"start":{"row":294,"column":6},"end":{"row":294,"column":7},"action":"insert","lines":["p"]},{"start":{"row":294,"column":7},"end":{"row":294,"column":8},"action":"insert","lines":["o"]},{"start":{"row":294,"column":8},"end":{"row":294,"column":9},"action":"insert","lines":["n"]},{"start":{"row":294,"column":9},"end":{"row":294,"column":10},"action":"insert","lines":["s"]},{"start":{"row":294,"column":10},"end":{"row":294,"column":11},"action":"insert","lines":["o"]},{"start":{"row":294,"column":11},"end":{"row":294,"column":12},"action":"insert","lines":["v"]}],[{"start":{"row":294,"column":11},"end":{"row":294,"column":12},"action":"remove","lines":["v"],"id":3492},{"start":{"row":294,"column":10},"end":{"row":294,"column":11},"action":"remove","lines":["o"]}],[{"start":{"row":294,"column":10},"end":{"row":294,"column":11},"action":"insert","lines":["i"],"id":3493},{"start":{"row":294,"column":11},"end":{"row":294,"column":12},"action":"insert","lines":["v"]},{"start":{"row":294,"column":12},"end":{"row":294,"column":13},"action":"insert","lines":["e"]},{"start":{"row":294,"column":13},"end":{"row":294,"column":14},"action":"insert","lines":["n"]},{"start":{"row":294,"column":14},"end":{"row":294,"column":15},"action":"insert","lines":["e"]},{"start":{"row":294,"column":15},"end":{"row":294,"column":16},"action":"insert","lines":["s"]},{"start":{"row":294,"column":16},"end":{"row":294,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":294,"column":20},"end":{"row":295,"column":0},"action":"insert","lines":["",""],"id":3494},{"start":{"row":295,"column":0},"end":{"row":296,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":291,"column":0},"end":{"row":294,"column":20},"action":"remove","lines":["    ","#=======================================================================#","","\"\"\"Responsiveness\"\"\""],"id":3495},{"start":{"row":290,"column":19},"end":{"row":291,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":243,"column":26},"end":{"row":243,"column":30},"action":"remove","lines":["POST"],"id":3496},{"start":{"row":243,"column":26},"end":{"row":243,"column":27},"action":"insert","lines":["G"]},{"start":{"row":243,"column":27},"end":{"row":243,"column":28},"action":"insert","lines":["E"]},{"start":{"row":243,"column":28},"end":{"row":243,"column":29},"action":"insert","lines":["T"]}],[{"start":{"row":243,"column":26},"end":{"row":243,"column":29},"action":"remove","lines":["GET"],"id":3497},{"start":{"row":243,"column":26},"end":{"row":243,"column":27},"action":"insert","lines":["P"]},{"start":{"row":243,"column":27},"end":{"row":243,"column":28},"action":"insert","lines":["O"]},{"start":{"row":243,"column":28},"end":{"row":243,"column":29},"action":"insert","lines":["S"]},{"start":{"row":243,"column":29},"end":{"row":243,"column":30},"action":"insert","lines":["T"]}],[{"start":{"row":274,"column":53},"end":{"row":275,"column":0},"action":"insert","lines":["",""],"id":3499},{"start":{"row":275,"column":0},"end":{"row":275,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":275,"column":8},"end":{"row":275,"column":12},"action":"insert","lines":["    "],"id":3500}],[{"start":{"row":275,"column":12},"end":{"row":275,"column":16},"action":"insert","lines":["    "],"id":3501}],[{"start":{"row":275,"column":16},"end":{"row":275,"column":20},"action":"insert","lines":["    "],"id":3502}],[{"start":{"row":275,"column":20},"end":{"row":275,"column":24},"action":"insert","lines":["    "],"id":3503}],[{"start":{"row":275,"column":24},"end":{"row":275,"column":28},"action":"insert","lines":["    "],"id":3504}],[{"start":{"row":275,"column":28},"end":{"row":275,"column":32},"action":"insert","lines":["    "],"id":3505}],[{"start":{"row":275,"column":32},"end":{"row":276,"column":61},"action":"insert","lines":["origins=mongo.db.origins.find(),","                        difficulty=mongo.db.difficulty.find()"],"id":3506}],[{"start":{"row":276,"column":61},"end":{"row":276,"column":62},"action":"insert","lines":[","],"id":3507}],[{"start":{"row":276,"column":62},"end":{"row":276,"column":63},"action":"insert","lines":[" "],"id":3508},{"start":{"row":276,"column":63},"end":{"row":277,"column":0},"action":"insert","lines":["",""]},{"start":{"row":277,"column":0},"end":{"row":277,"column":24},"action":"insert","lines":["                        "]}],[{"start":{"row":277,"column":24},"end":{"row":277,"column":28},"action":"insert","lines":["    "],"id":3509}],[{"start":{"row":275,"column":28},"end":{"row":275,"column":32},"action":"remove","lines":["    "],"id":3510}],[{"start":{"row":275,"column":28},"end":{"row":275,"column":32},"action":"insert","lines":["    "],"id":3511}],[{"start":{"row":275,"column":28},"end":{"row":275,"column":32},"action":"remove","lines":["    "],"id":3512}],[{"start":{"row":276,"column":24},"end":{"row":276,"column":28},"action":"insert","lines":["    "],"id":3513}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":46},"action":"remove","lines":["app.config['SECRET_KEY'] = 'the random string'"],"id":3514},{"start":{"row":12,"column":48},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":48},"end":{"row":12,"column":48},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1572686333075,"hash":"39e90a24ffdb5b91f9ffd9926eb80830a9fa8db3"}
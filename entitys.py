class Entity:
    def __init__(self, data):
        self.data = data;
        self.resources = data["resources"]
        self.activeAffects = []
    def attack(self):
        #where target is special condition maybe I dunno
        baseAttack = self.data["basic_attack"]
        multiplier = sum([self.data["stats"][statMultiplier["name"]] * statMultiplier["multiplier"] for statMultiplier in baseAttack["stat_multipliers"]])
        for cost in baseAttack["costs"]:
            for key in cost.keys():
                self.resources[key] -= cost[key]
        a = {
                "base_damage": baseAttack["base_damage"] * multiplier,
                "affects": baseAttack["affects"]
            }
        return a
    def hit(self, attack):
        #where attack is a dict with attack info like affects
        self.resources["health"] -= attack["base_damage"]
        tempList = []
        for affect in attack["affects"]:
            isInActiveAffects = False
            for activeAffect in self.activeAffects:
                if affect["name"] == activeAffect["name"]:
                    activeAffect["stacks"] += 1
                    isInActiveAffects = True
                    break
            if not isInActiveAffects:
                tempList.append(affect)
        self.activeAffects.extend(tempList)

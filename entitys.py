class Entity:
    def __init__(self, data):
        self.data = data;
        self.resources = data["resources"]
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
        #where attack is a dict with attack info 
        pass

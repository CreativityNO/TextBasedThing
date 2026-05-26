class Entity:
    def __init__(self, data):
        self.data = data;

    def attack(self):
        #where target is special condition maybe I dunno
        #this can be handled later because of various conditions with an attack like how distance affects the attack this should just return damage 
        #the hit should also process affects 
        #entity should just deal with itself so the combat handler can focus on just inputing the right things
        #distance will be handled here but not calculated here
        #Hmmmm
        #An attack skill will have very similar code
        #I could perhaps make it more modular
        baseAttack = self.data["basic_attack"]
        multiplier = sum([self.data["stats"][stat] * multiplier for (stat, multiplier) in baseAttack["stat_multipliers"]])
        for (resource, cost) in baseAttack["costs"]:
            self.data["resources"][resource] -= cost
        a = {
                "base_damage": baseAttack["base_damage"] * multiplier,
                "affects": baseAttack["affects"]
            }
        return a
    def attack(self,info):
        #where target is special condition maybe I dunno
        #this can be handled later because of various conditions with an attack like how distance affects the attack this should just return damage 
        #the hit should also process affects 
        #entity should just deal with itself so the combat handler can focus on just inputing the right things
        #distance will be handled here but not calculated here
        #Hmmmm
        #An attack skill will have very similar code
        #I could perhaps make it more modular
        baseAttack = info
        statMultiplier = sum([self.data["stats"][stat] * multiplier for (stat, multiplier) in baseAttack["stat_multipliers"]])
        for (resource, cost) in baseAttack["costs"]:
            self.data["resources"][resource] -= cost
        a = {
                "base_damage": baseAttack["base_damage"] * statMultiplier,
                "affects": baseAttack["affects"]
            }
        return a
    def hit(self, attack):
        #just lower health
        #self.data["resources"]["health"] -= attack
        #where attack is a dict with attack info like affects
        self.data["resources"]["health"] -= attack["base_damage"]
        #tempList = []
        for (name,stack) in attack["affects"]:
            if name in self.data["active_affects"]:
                self.data["active_affects"][name] += stack
            else:
                self.data["active_affects"][name] = stack
        #    isInActiveAffects = False
        #     for activeAffect in self.data["active_affects"]:
        #         if affect["name"] == activeAffect["name"]:
        #             activeAffect["stacks"] += 1
        #             isInActiveAffects = True
        #             break
        #     if not isInActiveAffects:
        #         tempList.append(affect)
        # self.activeAffects.extend(tempList)
    def useSkill(self, skillName):
        #targeting must happen here because of specific requirements and so it happens in everything else
        #how will targeting work
        #I will have to make the combat handler then but not now
        #perhaps
        #an attack skill vs heal or buff or util
        #do i do it all here?
        #yes so again simpler on the handlers side
        #but how to do targeting
        #
        # 0 = attack
        # 1 = heal
        # 2 = effect so buff or debuff or taunt
        if skillName in self.data["skills"]:
            if self.data["skills"][skillName]["type"] == 0:
                self.attack(self.data["skills"][skillName])
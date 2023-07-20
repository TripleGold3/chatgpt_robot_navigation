

class generate_message:
    def __init__(self):
        self.messages=[{"role": "system", "content": "你是一个助手"}]
        self.content = ""
        
    def generate_robot_prompt(self,coordinates):
        prompt = "以下是机器人的坐标：\n"

        for i, (x, y) in enumerate(coordinates, 1):
            prompt += f"机器人{i}位于坐标({x}, {y})。\n"
        return prompt
    
    def generate_target_prompt(self, coordinates):
        prompt = "以下是目标位置的坐标：\n"

        for i, (x, y) in enumerate(coordinates, 1):
            prompt += f"目标{i}位于坐标({x}, {y})。\n"
        return prompt
    
    def generate_prompt(self,coordinates, target_coordinates):
        prompt = self.generate_robot_prompt(coordinates)
        prompt += self.generate_target_prompt(target_coordinates)
        prompt += "请给机器人分配目标位置\n"
        prompt += "结果格式为：机器人编号->目标位置"
        return prompt
    

    

if __name__ == '__main__':
    coordinates = [(1,1), (2,5), (5,6), (8,3)]
    target_coordinates = [(1,3), (9,5), (4,6), (3,9)]
    print(generate_message().generate_prompt(coordinates, target_coordinates))
        
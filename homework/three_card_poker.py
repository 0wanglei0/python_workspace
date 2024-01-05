import random
from collections import Counter


def start_post_card(_pokers):
# 发牌
    for _ in range(0, 3):
        # 顺次发牌
        for the_player in players_pokers.keys():
            post_card = random.randint(0, len(_pokers) - 1)
            players_pokers[the_player].append(_pokers[post_card])
            _pokers.pop(post_card)


# 当手牌数字相同，增加花色权重
def add_weight(is_weight, keys):
    if not is_weight:
        return [1, 1, 1]
    total_weight = []
    for color in keys:
        if color == "spades":
            weight = 4
        elif color == "Hearts":
            weight = 3
        elif color == "diamonds":
            weight = 2
        else:
            weight = 1

        total_weight.append(weight)
    return total_weight


# 豹子
def leopard(values, is_record):
    if is_record:
        record_type["leopard"] = record_type["leopard"] + 1
    return values[0] * 100000000


# 对子大小
def pair(values, card_keys, is_weight, is_record):
    if is_record:
        record_type["pair"] = record_type["pair"] + 1
    counts = Counter(values)
    weight = add_weight(is_weight, card_keys)
    most_common_element = counts.most_common(1)[0][0]  # 要知道重复的是哪个元素,这里元素的最大次数肯定是2
    least_common_element = counts.most_common()[-1][0]  # 最少的元素既是单独的哪个元素
    pair_index = values.index(most_common_element)
    if pair_index == 0:
        return max(weight[0], weight[1]) * most_common_element * 100 + weight[2] * least_common_element * 1  # 最大单子：[J,K,A]=143.2,最小对子:[2,2,3]=203
    else:
        return max(weight[1], weight[2]) * most_common_element * 100 + weight[0] * least_common_element * 1  # 最大单子：[J,K,A]=143.2,最小对子:[2,2,3]=203


# 同花顺判断
def straight_flush(keys, values, is_weight, is_record):
    weight = add_weight(is_weight, keys)
    if len(set(keys)) == 1:
        # 同花顺
        if values[0] + 1 == values[1] and values[1] + 1 == values[2]:
            if is_record:
                record_type["straight_flush"] += 1
            return weight[2] * values[2] * 800000 + weight[1] * values[1] * 10 + values[0] * weight[0]
        else:
            # 同花
            if is_record:
                record_type["decor"] += 1
            return weight[2] * values[2] * 300000 + weight[1] * values[1] * 10 + weight[0] * values[0]
    else:
        # 顺子
        if values[0] + 1 == values[1] and values[1] + 1 == values[2]:
            if is_record:
                record_type["sequence"] += 1
            return weight[2] * values[2] * 3000 + weight[1] * values[1] * 1 + weight[0] * values[0] * 0.1
        else:
            # 单张
            if is_record:
                record_type["one_card"] += 1
            return weight[2] * values[2] * 10 + weight[1] * values[1] * 1 + weight[0] * values[0] * 0.1


# 比大小
def get_winner(_players_pokers, is_weight, is_record):
    for player, poker in _players_pokers.items():
        card_keys = []
        card_values = []
        for cards in poker:
            for color in cards.keys():
                card_keys.append(color)
            for card in cards.values():
                if card == 'A':
                    card = 14
                elif card == 'J':
                    card = 11
                elif card == 'Q':
                    card = 12
                elif card == 'K':
                    card = 13
                card_values.append(card)

        sorted_value = sorted(card_values)

        if len(set(card_values)) == 1:
            results[player] = leopard(sorted_value, is_record)
        elif len(set(card_values)) == 2:
            results[player] = pair(sorted_value, card_keys, is_weight, is_record)
        else:
            results[player] = straight_flush(card_keys, sorted_value, is_weight, is_record)


def print_winner(output_winner):
    winner_player.clear()

    max_poker = max(results.values())
    for key, value in results.items():
        if value == max_poker:
            winner_player.append(key)
        else:
            loser_player.append(key)

    if len(winner_player) == 1:
        print("winner is：{winner}".format(winner=winner_player[0]))
        print("pokers is：{pokers}".format(pokers=players_pokers[winner_player[0]]))
        print()

        if not output_winner:
            return

        for loser in loser_player:
            print("loser is：{loser}".format(loser=loser))
            print("others pokers is：{pokers}".format(pokers=players_pokers[loser]))
            print()
    else:
        results.clear()
        player_poker = {}
        for winner in winner_player:
            player_poker[winner] = players_pokers[winner]
            print("same is ", players_pokers[winner])
        print()

        get_winner(player_poker, True, False)
        print_winner(output_winner)
        record_type["same_card"] = record_type["same_card"] + 1


if __name__ == '__main__':
    # 定义牌型
    decors = ["Hearts", "spades", "diamonds", "clubs"]
    poker_nums = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    # 各种牌型出现的次数
    record_type = {"leopard": 0, "pair": 0, "straight_flush": 0, "decor": 0, "sequence": 0, "one_card": 0, "same_card": 0}
    # 定义玩家
    # 结果，计分形式比较
    results = {}
    winner_player = []
    loser_player = []
    i = 0
    while i < 1000:
        # 生成52张牌
        all_pokers = []
        for item in decors:
            for num in poker_nums:
                num_dict = {item: num}
                all_pokers.append(num_dict)
        players_pokers = {"actor_1": [], "actor_2": [], "actor_3": [], "actor_4": [], "actor_5": []}
        start_post_card(all_pokers)
        # 比大小
        get_winner(players_pokers, False, True)
        # 输出结果
        print_winner(False)
        i += 1

    total = 0
    for key, value in record_type.items():
        if key != "same_card":
            total += value
        print(f"{key} 一共有 {value} 次")
        print()
    print(total)

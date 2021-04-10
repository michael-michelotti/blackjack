def handle_initial_deal(table):
    dealer = table.dealer
    dealer.deal_self_cards(2)

    print(f'Dealer\'s Card:')
    for player in table.players:
        dealer.deal_cards(2, player)

    return table

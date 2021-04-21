def handle_initial_deal(table):
    dealer = table.dealer
    dealer.deal_cards(2, to_self=True)

    print('Dealer\'s Cards:')
    for player in table.players:
        dealer.deal_cards(2, player)

    return table

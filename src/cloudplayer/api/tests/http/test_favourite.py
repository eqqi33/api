import pytest


@pytest.mark.gen_test
async def test_favourite_id_should_be_referenced_in_account(
        account, user_fetch):
    response = await user_fetch(
        '/account/cloudplayer/{}'.format(account.id))
    favourite_id = response.json().get('favourite_id')
    assert favourite_id == account.favourite.id
    response = await user_fetch(
        '/favourite/cloudplayer/{}'.format(favourite_id))
    account_id = response.json().get('account_id')
    assert account_id == account.id

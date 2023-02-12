from behave import *
from services.selenium_service import SeleniumService
from services.add_user_service import AddUserService
from services.list_user_service import ListUserService
from services.delete_user_service import DeleteUserService
from helpers.string_helper import StringHelper
from entities.list_user import ListUser

@given("I open protractor practice website")
def given_i_open_protractor_practice_website(context):
    selenium_service = SeleniumService(context)
    selenium_service.visit_page('https://www.way2automation.com/angularjs-protractor/webtables/')

@When("I add a new user")
def when_i_add_a_new_user(context):
    add_service = AddUserService(context)
    list_service = ListUserService(context)
    list_service.click_add_user()
    row = context.table[0]
    add_service.add_user(first_name=row['first_name'], last_name=row['last_name'], user_name=row['user_name'], password=row["password"],
                    customer=row['customer'], role=row['role'], email=row["email"], cell_phone=row['cellphone'])

@Then("I see the user has been added to the table")
def then_i_see_the_user_has_been_added_to_the_table(context):
    list_service = ListUserService(context)
    row = context.table[0]
    expected_user = ListUser(first_name=row['first_name'], last_name=row['last_name'], user_name=row['user_name'],
                    customer=row['customer'], role=row['role'], email=row["email"], cell_phone=row['cellphone'], locked=StringHelper.string_to_bool(row["locked"]))
    actual_user = list_service.get_actual_user(expected_user.user_name)
    assert expected_user == actual_user

@When("I delete user {user}")
def when_i_delete_user(context, user):
    delete_service = DeleteUserService(context)
    delete_service.delete_user(user)

@Then("I see the user {user} has been deleted from the user list")
def then_i_see_the_user_has_been_deleted_from_the_user_list(context, user):
    list_service = ListUserService(context)
    actual_user = list_service.get_actual_user(user)
    assert actual_user == "Not Found"

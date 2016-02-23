from testrail import APIClient as A
import Common as C

class Cases:
    def __init__(self):
        self.a = A(C.base_url)
        self.a.user = C.user
        self.a.password = C.password

    #Requires caseid as input
    def get_case(self,caseid):
        return self.a.send_get('get_case/'+str(caseid))

    #Requires projectid , sectionid, caseid as input parameters
    def get_cases(self,project_id,suite_id,section_id):
        return self.a.send_get('get_cases/'+str(project_id)+'&suite_id='+str(suite_id)+'&section_id='+str(section_id))

    #Requires sectionid as input and valid data for the case,you can get a sample data by using get_case
    def add_case(self,section_id,data):
        return self.a.send_post('add_case/'+str(section_id),data)

    #Requires caseid as input and data should be appropriate, you can get a sample data by using get_case
    def update_case(self,case_id,data):
        return self.a.send_post('update_case/'+str(case_id),data)

    #Requires caseid as input
    def delete_case(self,case_id):
        return self.a.send_post('delete_case/'+str(case_id),{})

    #This function returns the different types of cases
    def get_case_types(self):
        return self.a.send_get('get_case_types')

    #This function returns the different types of fields
    def get_case_fields(self):
        return self.a.send_get('get_case_fields')


class Projects:
    def __init__(self):
        self.a = A(C.base_url)
        self.a.user = C.user
        self.a.password = C.password

    #Requires projectid as input
    def get_project(self,project_id):
        return self.a.send_get('get_project/'+str(project_id))

    #gives info about all the projects
    def get_projects(self,project_id):
        return self.a.send_get('get_projects')

    #Requires Project name
    def add_project(self,name):
        return self.a.send_post('add_project',name)

    #Requires Project name
    def update_project(self,project_id,data):
        return self.a.send_post('update_project/'+str(project_id),data)

    #this deletes a project with given id
    def delete_project(self,project_id):
        return self.a.send_post('delete_project/'+str(project_id),{})

class Section:
    def __init__(self):
        self.a = A(C.base_url)
        self.a.user = C.user
        self.a.password = C.password

    #Requires sectionid as input
    def get_section(self,section_id):
        return self.a.send_get('get_section/'+str(section_id))

    #Returns sections in suite for the mentioned project
    def get_sections(self,project_id,suite_id):
        return self.a.send_get('get_sections/'+str(project_id)+'&'+'suite_id='+str(suite_id))

    #Requires project name to add a section
    def add_section(self,project_id,data):
        return self.a.send_post('add_section/'+str(project_id),data)

    #Requires Project name
    def update_section(self,section_id,data):
        return self.a.send_post('update_section/'+str(section_id),data)

    #this deletes a project with given id
    def delete_section(self,section_id):
        return self.a.send_post('delete_section/'+str(section_id),{})

class Suites:
    def __init__(self):
        self.a = A(C.base_url)
        self.a.user = C.user
        self.a.password = C.password

    #Requires suiteid as input
    def get_suite(self,suite_id):
        return self.a.send_get('get_suite/'+str(suite_id))

    #Returns suite for the mentioned project
    def get_suites(self,project_id):
        return self.a.send_get('get_suites/'+str(project_id))

    #Requires project id to add a suite
    def add_suite(self,project_id,data):
        return self.a.send_post('add_suite/'+str(project_id),data)

    #Requires suiteid and data for updation
    def update_suite(self,suite_id,data):
        return self.a.send_post('update_suite/'+str(suite_id),data)

    #this deletes a suite with given id
    def delete_suite(self,suite_id):
        return self.a.send_post('delete_suite/'+str(suite_id),{})

class Results:
    def __init__(self):
        self.a = A(C.base_url)
        self.a.user = C.user
        self.a.password = C.password

    #Requires testid as input to get the results
    def get_results(self,test_id):
        return self.a.send_get('get_results/'+str(test_id))

    #Returns results for a given case
    def get_results_for_case(self,run_id,case_id):
        return self.a.send_get('get_results_for_case/'+str(run_id)+'/'+str(case_id))

    #Returns results for a given run
    def get_results_for_run(self,run_id):
        return self.a.send_get('get_results_for_run/'+str(run_id))

    #Requires test id and data to add a result
    def add_result(self,test_id,data):
        return self.a.send_post('add_result/'+str(test_id),data)

    #Requires runid, testid, data to add result for case
    def add_result_for_case(self,run_id,case_id,data):
        return self.a.send_post('add_result_for_case/'+str(run_id)+'/'+str(case_id),data)

    #Adds one or more new test results, comments or assigns one or more tests. Ideal for test automation to bulk-add multiple test results in one step.
    def add_results(self,run_id):
        return self.a.send_post('add_results/'+str(run_id),{})

    #adds results for a given run id, here is sample data for same
    '''
{
	"results": [
		{
			"case_id": 1,
			"status_id": 5,
			"comment": "This test failed",
			"defects": "TR-7"

		},
		{
			"case_id": 2,
			"status_id": 1,
			"comment": "This test passed",
			"elapsed": "5m",
			"version": "1.0 RC1"
		},

		..

		{
			"case_id": 1,
			"assignedto_id": 5,
			"comment": "Assigned this test to Joe"
		}

		..
	]
}'''
    def add_results_for_cases(self,run_id,data):
        return self.a.send_post('add_results_for_cases/'+str(run_id),data)

    #Return all different results fields available
    def get_result_fields(self):
        return self.a.send_get('get_result_fields/')


class Runs:
    def __init__(self):
        self.a = A(C.base_url)
        self.a.user = C.user
        self.a.password = C.password

    #Returns an existing test run
    def get_run(self,run_id):
        return self.a.send_get('get_run/'+str(run_id))

    #Returns an existing test run
    def get_runs(self,project_id):
        return self.a.send_get('get_runs/'+str(project_id))

    #Returns a list of test runs for a project. Only returns those test runs that are not part of a test plan
    def add_run(self,project_id,data):
        return self.a.send_post('add_run/'+str(project_id),data)

    #Updates an existing test run (partial updates are supported, i.e. you can submit and update specific fields only).
    def update_run(self,run_id,data):
        return self.a.send_post('update_run/'+str(run_id),data)

    #Closes an existing test run and archives its tests & results.
    def close_run(self,run_id):
        return self.a.send_post('close_run/'+str(run_id),{})

    #Deletes an existing test run.
    def delete_run(self,run_id):
        return self.a.send_post('delete_run/'+str(run_id),{})


class Test:
    def __init__(self):
        self.a = A(C.base_url)
        self.a.user = C.user
        self.a.password = C.password

    #Returns an existing test.
    def get_test(self,test_id):
        return self.a.send_get('get_test/'+str(test_id))

    #Returns a list of tests for a test run.
    def get_tests(self,run_id):
        return self.a.send_get('get_tests/'+str(run_id))


class Template:
    def __init__(self):
        self.a = A(C.base_url)
        self.a.user = C.user
        self.a.password = C.password

    #Returns a list of available templates (requires TestRail 5.2 or later).
    def get_templates(self,project_id):
        return self.a.send_get('get_templates/'+str(project_id))

class Users:
    def __init__(self):
        self.a = A(C.base_url)
        self.a.user = C.user
        self.a.password = C.password

    # Returns an existing user by given id
    def get_user(self,user_id):
        return self.a.send_get('get_user/'+str(user_id))

    #Returns an existing user by his/her email address.
    def get_user_by_email(self,email):
        return self.a.send_get('get_user_by_email&email'+str(email))

    # Returns a list of users.
    def get_users(self):
        return self.a.send_get('get_users')


class Plans:
    def __init__(self):
        self.a = A(C.base_url)
        self.a.user = C.user
        self.a.password = C.password

    #Returns an existing test plan.
    def get_plan(self,plan_id):
        return self.a.send_get('get_plan/'+str(plan_id))

    #Returns a list of test plans for a project.
    def get_plans(self,project_id):
        return self.a.send_get('get_plans/'+str(project_id))

    #Creates a new test plan.
    def add_plan(self,project_id,data):
        return self.a.send_post('add_plan/'+str(project_id),data)

    #Creates a new test plan.
    def add_plan_entry(self,plan_id,data):
        return self.a.send_post('add_plan_entry/'+str(plan_id),data)

    #Updates an existing test run (partial updates are supported, i.e. you can submit and update specific fields only).
    def update_plan(self,plan_id,data):
        return self.a.send_post('update_plan/'+str(plan_id),data)

    #Updates one or more existing test runs in a plan (partial updates are supported, i.e. you can submit and update specific fields only).
    def update_plan_entry(self,plan_id,entry_id,data):
        return self.a.send_post('update_plan_entry/'+str(plan_id)+'/'+str(entry_id),data)

    #Closes an existing test plan and archives its test runs & results.
    def close_plan(self,plan_id):
        return self.a.send_post('close_plan/'+str(plan_id),{})

    #Deletes an existing test plan.
    def delete_plan(self,plan_id):
        return self.a.send_post('delete_plan/'+str(plan_id),{})

    #Deletes one or more existing test runs from a plan.
    def delete_plan_entry(self,plan_id,entry_id):
        return self.a.send_post('delete_plan_entry/'+str(plan_id)+'/'+str(entry_id),{})





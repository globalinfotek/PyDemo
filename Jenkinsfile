pipeline {
    agent any

    triggers {
        pollSCM('*/5 * * * 1-5')
    }

    options {
        skipDefaultCheckout(true)
        // Keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }



    stages {

        stage ("Code pull"){
            steps{
                git url: 'git@github.com:globalinfotek/PyDemo.git'
            }
        }

        stage('Build environment') {
            steps {
                echo "Building virtualenv"
                sh  ''' python3 -m venv env
                        source ./env/bin/activate
                        pip install pytest-xdist
                        pip install pytest-cov
                    '''
            }
        }

        stage('Static code metrics') {
            steps {
                echo "Raw metrics"
               
                echo "Test and test coverage"
                sh  ''' source ./env/bin/activate
                        pytest --cov=ShoppingCart  TestShoppingCart.py
                        pytest --junitxml=reports/results/test_results.xml TestShoppingCart.py
                    '''
            }
        }



        stage('Unit tests') {
            steps {
                sh  ''' source ./env/bin/activate
                		    pytest  -vs TestShoppingCart.py 
                        pytest --junitxml=build/reports/results/test_results.xml TestShoppingCart.py
                    '''
            }
            post {
                always {
                    junit 'build/reports/**/*.xml'
                }
            }
        }
      
      stage('JIRA Interaction ') {
           steps {
                 script {
                    echo " Updating JIRA"
                    echo "Connecting with jira"
                    withEnv(['JIRA_SITE=GITI_JIRA']) {
                    def searchResults = jiraJqlSearch jql: "project = UDD AND issuekey = 'UDD-9' " 
                    def issues = searchResults.data.issues
                    for (i = 0; i <issues.size(); i++) {
                        def result = jiraGetIssue idOrKey: issues[i].key
                        result.data.fields.last_comment = 'New Build Ran'
                        response = jiraEditIssue idOrKey: issues[i].key
                    }
                 }
               }
            }
      }
    }
}
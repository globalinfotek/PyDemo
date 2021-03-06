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
                git url: 'git@github.com:globalinfotek/demo-python-app.git'
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
                    echo " Updating JIRA Isse with a Comment"
                    echo "Build Number  ${BUILD_NUMBER}  ':'  ${BRANCH_NAME} "
                    echo "Connecting with jira" 
                    def workingIssueName = env.BRANCH_NAME.split("_");
                    workingIssueName = (workingIssueName.length >0)?workingIssueName[0]:workingIssueName
                    workingIssueName = (workingIssueName == 'master')?"UDD-12":"UDD-12"
                    echo "Connecting with jira" +workingIssueName
                    withEnv(['JIRA_SITE=GITI_JIRA']) {
                        def searchResults = jiraJqlSearch jql: "project = UDD AND issuekey = '"+workingIssueName+"'"
                        def issues = searchResults.data.issues
                        for (i = 0; i <issues.size(); i++) {
                            def result = jiraGetIssue idOrKey: issues[i].key
                            def commentValue = "Some Comment FROM Build ${BUILD_NUMBER} TO BRANCH " +workingIssueName
                            response = jiraAddComment idOrKey: issues[i].key , comment: commentValue
                        }
                    }
               }
            }
      }
    }
}
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
                		    pytest  -vs TestShoppingCart.py 
                        pytest --cov=ShoppingCart  TestShoppingCart.py
                    '''
            }
            post{
                always{
                    step([$class: 'CoberturaPublisher',
                                   autoUpdateHealth: false,
                                   autoUpdateStability: false,
                                   coberturaReportFile: 'reports/coverage.xml',
                                   failNoReports: false,
                                   failUnhealthy: false,
                                   failUnstable: false,
                                   maxNumberOfBuilds: 10,
                                   onlyStable: false,
                                   sourceEncoding: 'ASCII',
                                   zoomCoverageChart: false])
                }
            }
        }



        stage('Unit tests') {
            steps {
                sh  ''' source ./env/bin/activate
                		    pytest  -vs TestShoppingCart.py 
                    '''
            }
        }

    

        stage('Build package') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                sh  ''' source activate ${BUILD_TAG}
                        python setup.py bdist_wheel
                    '''
            }
            post {
                always {
                    // Archive unit tests for the future
                    archiveArtifacts allowEmptyArchive: true, artifacts: 'dist/*whl', fingerprint: true
                }
            }
        }
    }

    post {
        always {
            sh 'conda remove --yes -n ${BUILD_TAG} --all'
        }
        failure {
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                         <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']])
        }
    }
}
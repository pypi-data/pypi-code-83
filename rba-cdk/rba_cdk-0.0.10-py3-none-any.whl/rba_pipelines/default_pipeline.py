import os
import pygit2

from aws_cdk import (
    core,
    aws_codepipeline as _codepipeline,
    aws_codepipeline_actions as _codepipeline_actions,
    aws_codecommit as _codecommit,
    aws_codebuild as _codebuild,
    pipelines as _pipelines
)

from rba_cdk import (
  rba_ecr,
  rba_codepipeline_actions,
  rba_utils
)

class PipelineStack(core.Stack):
  '''
  stack include an AWS codepipeline-based pipeline that has one CodeBuild stage that builds according to buildspec.yml.
  this stack class is opinionated.  it creates following construct based on the CodeCommit repository name:
    Default Build Stage - add a stage for CodeBuild that builds according to buildspec.yml.  
  '''  
  def __init__(self, scope: core.Construct, code_repo_name: str, **kwargs):
    branch_name = rba_utils.get_branch_name()
    '''
    branch_name is dynamically generated during class instantiation, not passed as an argument. 
    the reason for this decision is to minimized the code in cdk.py
    '''
    id = f'{code_repo_name}-{branch_name}'
    print(f'creating cdk.out for repository: {code_repo_name}, branch: {branch_name}')
    print(f'stack id: {id}')
    super().__init__(scope, id, **kwargs)

    source_artifact = _codepipeline.Artifact()
    cloud_assembly_artifact = _codepipeline.Artifact()
    build_artifact = _codepipeline.Artifact()
    codecommit_repo = _codecommit.Repository.from_repository_name(self, 'repo', code_repo_name)

    pipeline = _pipelines.CdkPipeline(self, f'{code_repo_name}-pipeline',
      cloud_assembly_artifact=cloud_assembly_artifact,
      pipeline_name=f'{code_repo_name}-{branch_name}',

      source_action=_codepipeline_actions.CodeCommitSourceAction(
        action_name='codeCommit',
        output=source_artifact,
        repository=codecommit_repo,
        branch=branch_name,
        variables_namespace='SourceVariables',
        code_build_clone_output=True),

      synth_action=_pipelines.SimpleSynthAction(
        source_artifact=source_artifact,
        cloud_assembly_artifact=cloud_assembly_artifact,
        install_commands=['npm install -g aws-cdk && pip install -r requirements.txt'],
        environment_variables={
          'COMMIT_ID': _codebuild.BuildEnvironmentVariable(value='#{SourceVariables.CommitId}'),
          'BRANCH_NAME': _codebuild.BuildEnvironmentVariable(value='#{SourceVariables.BranchName}')
        },
        synth_command='cdk synth --quiet'))
    
    build_stage = pipeline.add_stage('asBuildspec')
    # create an action to build the docker image
    build_action = rba_codepipeline_actions.DefaultBuildAction(self,
      action_name='CodeBuild',
      input=source_artifact,
      outputs=[build_artifact],
      variables_namespace='BuildVariables'
    )
    build_stage.add_actions(build_action)

    self.pipeline = pipeline
    self.build_artifact = build_artifact
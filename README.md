## Pragmatic AI sample app

Sample app from chapter 2 of Pragmatic AI book.

Includes a S3 client; jupyter notebook that uses the client; cli tool for downloading the data csv file; and tests.


## To run on AWS CodeBuild:

* Need to create project and pipeline first.

	CodeBuild will setup the webhooks for you when you specify Github as the source. 

* Under the section on 'Environment Image', set `Custom Image type` to `Other` and specify `Custom Image ID` of `python:3.6.2-stretch`

* Under `Build Specification` select `Use buildspec.yml in source code root directory`

If the build goes well, you should see the screenshot below:

![AWS Codebuild](https://github.com/cheeyeo/pragaipractice/AWS_CODEBUILD.png)



## Notes

Need to export PYTHONPATH for local dev
```
export PYTHONPATH="paws"
```
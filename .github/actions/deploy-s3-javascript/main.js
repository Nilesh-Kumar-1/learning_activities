const core=require('@actions/core');
const github=require('@actions/github');
const exec=require('@actions/exec');
function run(){
    //  TO get the required values
    const bucket = core.getInput('bucket', { require:true});
    const bucketRegion = core.getInput('bucket-region', {require:true});
    const distFolder = core.getInput('github-token', { required: true });

    // 2) Upload files exec package is used to run command in aws cli
    const s3Uri = `s3://${bucket}`
    exec.exec(`aws s3 sync ${distFolder} ${s3Uri} --region ${bucketRegion}`)

    const websiteUrl = `http://${bucket}.s3-website-${bucketRegion}.amazonaws.com`
    core.setOutput('website_url', websiteUrl)
    core.notice('Hello from my custom javascript actions')
}

run();
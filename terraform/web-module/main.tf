

resource "aws_amplify_app" "pplans_web_page" {
  name = "pplans_web_page"
  repository = var.repository
  access_token = var.access_token

  # The default build_spec added by the Amplify Console for React.
  build_spec = <<-EOT

    version: 0.2

    frontend:
      phases:
        preBuild:
          commands:
            - npm install
        build:
          commands:
            - npm run build
      artifacts:
        baseDirectory: dist
        files:
          - '**/*'
      cache:
        paths:
          - node_modules/**/*

    appRoot: src/web-app

  EOT

  # The default rewrites and redirects added by the Amplify Console.
  custom_rule {
    source = "/<*>"
    status = "404"
    target = "/index.html"
  }

  environment_variables = {
    ENV = "prod"
  }
}



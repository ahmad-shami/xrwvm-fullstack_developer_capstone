// URLs shoould not end with slashes /

const environments = {
    production: {
        nodejs_api_url: "http://94.203.133.222:3030",
        django_api_url: "http://94.203.133.222:8000",
        frontend_url: "http://dealership.ahmad.alshami.website:3000"
    },
    development: {
        nodejs_api_url: "http://dealership.ahmad.alshami.website:3030",
        django_api_url: "http://dealership.ahmad.alshami.website:8000",
        frontend_url: "http://dealership.ahmad.alshami.website:3000"
    },
};

const getEnvironment = environments.production;

export { getEnvironment };
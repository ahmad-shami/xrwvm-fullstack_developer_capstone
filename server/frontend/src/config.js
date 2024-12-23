// URLs shoould not end with slashes /

const environments = {
    production: {
        nodejs_api_url: "https://shamiahmad-3030.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai",
        django_api_url: "https://shamiahmad-8000.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai",
        frontend_url: "https://shamiahmad-3030.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai"
    },
    development: {
        nodejs_api_url: "http://dealership.ahmad.alshami.website:3030",
        django_api_url: "http://dealership.ahmad.alshami.website:8000",
        frontend_url: "http://dealership.ahmad.alshami.website:3000"
    },
};

const getEnvironment = environments.production;

export { getEnvironment };
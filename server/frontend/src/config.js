// URLs shoould not end with slashes /

const environments = {
    production: {
        nodejs_api_url: "https://shamiahmad-3030.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai",
        django_api_url: "https://shamiahmad-8000.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai",
        frontend_url: "https://shamiahmad-8000.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai"
    },
    development: {
        nodejs_api_url: "http://127.0.0.1:3030",
        django_api_url: "http://127.0.0.1:8000",
        frontend_url: "http://127.0.0.1:3000"
    },
};

const getEnvironment = environments.production;

export { getEnvironment };
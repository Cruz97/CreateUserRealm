const credentials = Credentials.usernamePassword('admindemobsc', 'V4zPU8FjL6kAf_X');
const user = await User.authenticate(credentials, 'https://demobsc.us1a.cloud.realm.io:9080');

const config = await GraphQLConfig.create({ 
  user: user,
  realmPath: '/NFC5'
});

const httpLink = concat(
    config.authLink,
    // Note: if using node.jclears, you'll need to provide fetch as well.
    new HttpLink({ uri: config.httpEndpoint })
  );

// Note: if using node.js, you'll need to provide webSocketImpl as well.
const subscriptionLink = new WebSocketLink({
  uri: config.webSocketEndpoint,
  options: {
    connectionParams: config.connectionParams,
  }
});

// Send subscription operations to the subscriptionLink and
// all others - to the httpLink
const link = split(({ query }) => {
    const { kind, operation } = getMainDefinition(query);
    return kind === 'OperationDefinition' && operation === 'subscription';
  },
  subscriptionLink,
  httpLink
);

client = new ApolloClient({
  link: link,
  cache: new InMemoryCache()
});

// You can now query the GraphQL API
const response = await client.query({
  query: gql`
    query {
      people(query: "age > 18", sortBy: "name") {
        name
        age
      }
    }
  `
});

const people = response.data.people;
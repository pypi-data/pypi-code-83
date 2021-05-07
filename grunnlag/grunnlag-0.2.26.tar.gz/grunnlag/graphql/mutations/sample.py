from bergen.query import DelayedGQL





CREATE_SAMPLE = DelayedGQL("""
mutation SampleCreate($name: String!) {
  createSample(name: $name){
    id
    name
    creator {
        username
    }
  }
}
""")
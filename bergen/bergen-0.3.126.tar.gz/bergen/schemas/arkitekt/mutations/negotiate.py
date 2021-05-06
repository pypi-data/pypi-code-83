from bergen.query import TypedGQL
from bergen.schema import Transcript


NEGOTIATION_GQL = TypedGQL("""

  mutation Negotiate(
      $clientType: ClientTypeInput!
      $inward: String,
      $outward: String,
      $port: Int,
      $version: String,
      $pointType: DataPointTypeInput,
      $needsNegotiation: Boolean
      
      ) {
  negotiate(
      clientType: $clientType,
      inward: $inward,
      outward: $outward,
      port: $port,
      version: $version,
      pointType: $pointType,
      needsNegotiation: $needsNegotiation
  ) {
    timestamp
    models {
        identifier
        point {
            app {
                name
            }
            id
            outward
            port
            type
            needsNegotiation
        }
    }
    postman {
        type
        kwargs
    }
    provider {
        type
        kwargs
    }
    host {
        type
        kwargs
    }
  }
  }
""", Transcript)
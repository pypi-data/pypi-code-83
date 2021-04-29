import inspect
import fnmatch
import click
from .util import KatState


@click.command()
@click.argument("query", required=False, nargs=-1)
@click.option(
    "--elements",
    is_flag=True,
    default=False,
    show_default=True,
    help="Show only elements.",
)
@click.option(
    "--commands",
    is_flag=True,
    default=False,
    show_default=True,
    help="Show only commands.",
)
@click.option(
    "--analyses",
    is_flag=True,
    default=False,
    show_default=True,
    help="Show only analyses.",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    default=False,
    show_default=True,
    help="Show extended documentation for each directive.",
)
@click.pass_context
def syntax(ctx, query, elements, commands, analyses, verbose):
    """Query the kat script syntax documentation.

    \b
    Simple wildcards are supported:

    - ``*`` matches 0 or more characters
    - ``?`` matches any single character
    - ``[abc]`` matches any characters in abc
    - ``[!abc]`` matches any characters not in abc

    Specify zero or more QUERY terms. By default, all syntax is shown.
    """
    from ..script import syntax
    from ..script.spec import KatSpec
    from ..script.adapter import ElementAdapter, CommandAdapter, AnalysisAdapter

    state = ctx.ensure_object(KatState)
    spec = KatSpec()

    if not elements and not commands and not analyses:
        directives = spec.directives
    else:
        directives = {}

        if elements:
            directives.update(spec.elements)
        if commands:
            directives.update(spec.commands)
        if analyses:
            directives.update(spec.analyses)

    adapters = set()
    for directive, adapter in directives.items():
        if query and not any(fnmatch.fnmatch(directive, q) for q in query):
            continue

        adapters.add(adapter)

    if not adapters:
        state.print_error("No directives found.")

    # Default colours for each directive type.
    colors = {ElementAdapter: "green", CommandAdapter: "yellow", AnalysisAdapter: "red"}

    # Sort the directives in order they appear in the spec. This is better than alphabetic sort,
    # which puts `x2axis` ahead of `xaxis`.
    order = list(directives)
    for adapter in sorted(
        adapters, key=lambda adapter: order.index(adapter.short_name)
    ):
        syntax_form = click.style(syntax(adapter.short_name))
        directive = " / ".join(sorted(adapter.aliases, key=lambda alias: len(alias)))
        fg = colors[type(adapter)]

        if verbose:
            if docstring := inspect.getdoc(adapter.docobj_type):
                # Grab only the first line of the docstring.
                doc = docstring.splitlines()[0]
            else:
                doc = "(no documentation)"

            state.print(directive, fg=fg)
            state.print("=" * len(directive), fg=fg)
            state.print(doc)
            state.print()
            state.print(syntax_form)
            state.print()
        else:
            state.print(f"{click.style(directive, fg=fg)}: {syntax_form}")


if __name__ == "__main__":
    syntax()
